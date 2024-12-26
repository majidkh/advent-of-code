import re

f = open("inputs/17.txt", "r")
lines = f.read().splitlines()
f.close()

programs = []
registers = {}
outputs = []

for line in lines:
    if line.startswith("Register"):
        r = re.findall(r"Register (\w): (\d+)", line)
        registers[r[0][0]] = int(r[0][1])

    if line.startswith("Program"):
        pr = re.findall(r"(\d+)", line)
        for p in pr:
            programs.append(int(p))

# Part 1
def get_operand_value ( operand_ ):
    if 0 <= operand_ <= 3:
        return operand_
    elif operand_ == 4:
        return registers["A"]
    elif operand_ == 5:
        return registers["B"]
    elif operand_ == 6:
        return registers["C"]
    elif operand_ == 7:
        return None

def run_command( opcode , operand , reg_a , reg_b , reg_c ):

    out_value = None
    jump = -1

    # division adv
    if opcode == 0:
        reg_a = int ( reg_a / (2** get_operand_value(operand) ) )

    # bxl bitwise XOR ( B , val) - OK
    if opcode == 1:
        reg_b = reg_b ^ operand

    # bst modulo 8
    if opcode == 2:
        reg_b = get_operand_value(operand) % 8

    # jnz
    if opcode == 3:
        if reg_a > 0:
            jump = operand

    # bxc bitwise XOR ( B , C ) - OK
    if opcode == 4:
        reg_b = reg_b ^ reg_c

    # out
    if opcode == 5:
        out_value = get_operand_value(operand) % 8

    # bdv
    if opcode == 6:
        reg_b = int(reg_a / (2 ** get_operand_value(operand)))

    # cdv
    if opcode == 7:
        reg_c = int(reg_a / (2 ** get_operand_value(operand)))

    return jump , out_value , reg_a , reg_b , reg_c

def run_application():
    outputs.clear()
    pointer = 0
    while True:
        opcode = programs[pointer]
        operand = programs[pointer + 1]

        jump, out_val, registers["A"], registers["B"], registers["C"] = run_command ( opcode , operand , registers["A"] , registers["B"] , registers["C"] )

        if out_val is not None:
            outputs.append( out_val )

        if len(outputs) > len(programs):
            break

        if jump >= 0:
            pointer = jump
        else:
            pointer += 2

        if pointer >= len(programs):
            break

    return outputs

run_application()
print("Part 1:", ",".join(map(str, outputs)) )

# Part 2
def calculate_registers( loop, value):
    for addition in range(8):

        registers["A"] = value * 8 + addition
        registers["B"] = registers["C"] = 0

        if run_application() == programs[loop:]:
            if loop == 0:
                return 8 * value + addition
            best = calculate_registers( loop - 1, value * 8 + addition)
            if best is not None:
                return best
    return None

print( "Part 2", calculate_registers( len(programs) - 1, 0))