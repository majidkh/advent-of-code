import re
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

# Run the whole commands with input data
def run_program ( formulas_ , variables ):

    result = {}

    while True:

        finished = True
        for key1 , operator, key2, var_out in formulas_:

            value1 = variables[key1] if key1 in variables else (result[key1] if key1 in result else None)
            value2 = variables[key2] if key2 in variables else (result[key2] if key2 in result else None)

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

    sorted_dict = {key: value for key, value in sorted(result.items())}

    bin_result = ""
    for key, value in sorted_dict.items():
        if key.startswith("z"):
            bin_result += str(value)

    return int(bin_result[::-1], 2)

# Run the program for part 1
z = run_program ( formulas , inputs )
print ("Part 1:" , z )

# Part 2
bin_x = bin_y = ""

for key, value in inputs.items():
    if key.startswith("x"):
        bin_x += str(value)
    if key.startswith("y"):
        bin_y += str(value)

x = int(bin_x[::-1],2)
y = int(bin_y[::-1],2)
bin_z = format(z, "b")

# Expected result after rewiring
e = x + y
bin_e = format(e, "b")

