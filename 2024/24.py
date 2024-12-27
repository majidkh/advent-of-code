import copy
import re
from functools import cache

f = open("inputs/24.txt", "r")
lines = f.read()
f.close()

inputs = {}
formulas = []

# Extract inputs
for line in lines:
    data = re.findall("(\w+): (\d+)", lines)
    for v in data:
        inputs[v[0]] = int(v[1])

# Extract formulas
data = re.findall("(\w+) (\w+) (\w+) -> (\w+)", lines)
for v in data:
    formulas.append([ v[0], v[1], v[2], v[3] ])

# Run a formula with 2 inputs and return the result
@cache
def calculate( v1, operator, v2 ):
    if operator == "AND":
        if v1 == 1 and v2 == 1:
            return 1
        else:
            return 0
    elif operator == "OR":
        if v1 == 1 or v2 == 1:
            return 1
        else:
            return 0
    elif operator == "XOR":
        if v1 != v2:
            return 1
        else:
            return 0
    return 0

# Run the whole commands with inputs data
def run_program ( formulas_ , input_vars ):

    result = {}

    loops = 0

    while True:
        loops +=1
        if loops > 100:
            return None

        finished = True
        for key1 , operator, key2, var_out in formulas_:

            value1 = input_vars[key1] if key1 in input_vars else (result[key1] if key1 in result else None)
            value2 = input_vars[key2] if key2 in input_vars else (result[key2] if key2 in result else None)

            # IF already processed skip
            if var_out in result and result[var_out] is not None: continue

            # If formula is not ready and missing inputs, skip
            if value1 is None or value2 is None:
                finished = False
                continue

            # Process the command
            res = calculate( value1 , operator , value2  )

            # Store the result only once
            if var_out not in result:
                result[ var_out] = res

        if finished:
            break

    return {k_: v_ for k_, v_ in sorted(result.items())}

def bin_run_program ( formulas_ , input_vars ):
    out = run_program ( formulas_ , input_vars )

    if out is None: return None

    binary_z = ""
    for k_, v_ in out.items():
        if k_.startswith("z"):
            binary_z += str(v_)
    return binary_z[::-1]

# Run the program for part 1
output = run_program ( formulas , inputs )

max_bits = 0

# Extract output value
bin_z = ""
for key, value in output.items():
    if key.startswith("z"):
        max_bits += 1
        bin_z += str(value)
bin_z = bin_z[::-1]
z = int(bin_z,2)

print ("Part 1:" , z  )

# Part 2

def fix_indent( binary_z , correct_bin ):
    if len(binary_z) > len(correct_bin):
        correct_bin = "0" * (len(binary_z) - len(correct_bin)) + correct_bin
    return correct_bin

bin_x = bin_y = ""
for key, value in inputs.items():
    if key.startswith("x"):
        bin_x += str(value)
    if key.startswith("y"):
        bin_y += str(value)

x = int(bin_x[::-1],2)
y = int(bin_y[::-1],2)

# Expected result after rewiring
e = x + y
bin_e = fix_indent( bin_z, format(e, "b") )

def de_compile (formulas_, input_vars, var_out, should_print = False, depth = 0, input_keys= []):

    for key1, operator, key2, out_ in formulas_:
        if out_ == var_out:

            if key1 not in input_keys : input_keys.append(key1)
            if key2 not in input_keys :input_keys.append(key2)

            value1 = input_vars[key1] if key1 in input_vars else None
            value2 = input_vars[key2] if key2 in input_vars else None

            if value1 is None and key1 in output:
                value1 = output[key1]
            if value2 is None and key2 in output:
                value2 = output[key2]

            fixed_output = None

            if value1 is not None and value2 is not None:
                fixed_output = calculate (value1, operator, value2)

            if should_print:
                if depth == 0 :
                    print ( key1 , operator , key2 , "=" , out_ , "[" , fixed_output , "]" )
                else:
                    print ( " " * (depth * 4) , key1 , operator , key2 , "=" , out_ , "[" , fixed_output , "]" )

            de_compile(formulas_, input_vars, key1, should_print, depth + 1 , input_keys )
            de_compile(formulas_, input_vars, key2, should_print, depth + 1 , input_keys)

    return input_keys

def get_score ( binary_z , correct_bin ):
    for index in range(len(binary_z)):
        if binary_z[ - (index+1)] != correct_bin[ - (index+1)]:
            return index
    return float("inf")

def swap_wires ( formulas_ , wire1 , wire2 ):

    for formula_ in formulas_:
        if formula_[3] == wire1:
            formula_[3] = wire2
        elif formula_[3] == wire2:
            formula_[3] = wire1

    return formulas_

def fix_wires ( formulas_ , inputs_ , swaps ):

    copy_form = copy.deepcopy(formulas_)

    for wire1,wire2 in swaps:
        swap_wires(copy_form , wire1, wire2)

    binary_z = bin_run_program( copy_form , inputs_ )
    if binary_z == bin_e:
        flattened = [wire for tup in swaps for wire in tup]
        print( swaps)
        print("Part 2:", ",".join(sorted(flattened)))
        quit()

    if len(swaps) >=4: return

    old_score = get_score( binary_z , bin_e )

    # Find first moving wire
    wire = f"z{old_score:02}"
    for key1, operator, key2, out_ in formulas_:
        if out_ == wire:
            if operator == "OR" and output[out_] == 0:
                wire = out_
            elif operator == "AND" and output[out_] == 0:
                wire = out_
            elif operator == "XOR" and output[out_] == 1:
                wire = key1

    candidates = de_compile( formulas_ , inputs_ , f"z{old_score+1:02}" , False )

    # Now find the first swap
    for new_wire in candidates: # First Fix

        if new_wire != wire:
            if new_wire.startswith("x"): continue
            if new_wire.startswith("y"): continue

            key_ok = True

            for key1, operator, key2, out_ in formulas_:
                if out_ == new_wire :
                    if operator != "XOR":
                        key_ok = False
                    else:
                        break

            if not key_ok: continue

            copy_form = swap_wires(copy_form , wire , new_wire )
            new_z_bin = bin_run_program(copy_form, inputs_)
            copy_form = swap_wires(copy_form , wire , new_wire )

            if new_z_bin is None: continue
            new_score = get_score( new_z_bin , bin_e)

            if new_score > old_score:
                old_score = new_score
                fix_wires ( formulas_, inputs_, swaps  + [ (wire , new_wire) ] )

fix_wires ( formulas , inputs , []  )

