import re

f = open("inputs/17.txt", "r")
lines = f.read().splitlines()
f.close()

programs = []
registers = {}
output = []

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

def run_program( instruction , val ):
    # division adv
    if instruction == 0:
        registers["A"] = int (registers["A"] / (2** get_operand_value(val) ) )

    # bxl bitwise XOR ( B , val) - OK
    if instruction == 1:
        registers["B"] = registers["B"] ^ val

    # bst modulo 8
    if instruction == 2:
        registers["B"] = get_operand_value(val) % 8

    # jnz
    if instruction == 3:
        if registers["A"] == 0:
            return -1
        elif registers["A"] > 0:
            # Jump the pointer
            return val

    # bxc bitwise XOR ( B , C ) - OK
    if instruction == 4:
        registers["B"] = registers["B"] ^ registers["C"]

    # out
    if instruction == 5:
        output.append (  get_operand_value(val) % 8 )

    # bdv
    if instruction == 6:
        registers["B"] = int(registers["A"] / (2 ** get_operand_value(val)))

    # cdv
    if instruction == 7:
        registers["C"] = int(registers["A"] / (2 ** get_operand_value(val)))

    return -1

def run_application():

    pointer = 0
    while True:
        opcode = programs[pointer]
        operand = programs[pointer + 1]
        jump = run_program ( opcode , operand )

        if jump >= 0:
            pointer = jump
        else:
            pointer += 2

        if pointer >= len(programs):
            break

run_application()
print("Part 1:", ",".join(map(str, output)) )
