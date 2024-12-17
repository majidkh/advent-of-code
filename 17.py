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

    #print("command", opcode , operand, reg_a, reg_b, reg_c)

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

    pointer = 0
    while True:
        opcode = programs[pointer]
        operand = programs[pointer + 1]

        jump, out_val, registers["A"], registers["B"], registers["C"] = run_command ( opcode , operand , registers["A"] , registers["B"] , registers["C"] )

        if out_val is not None:
            outputs.append( out_val )

        if jump >= 0:
            pointer = jump
        else:
            pointer += 2

        if pointer >= len(programs):
            break


run_application()
print("Part 1:", ",".join(map(str, outputs)) )
print(registers)

# Part 2
outputs = programs
print(outputs)

def run_reverse_command( opcode , operand , out_value , reg_a , reg_b , reg_c ):

    output_index_move = 0

    #print("command", opcode , operand, reg_a, reg_b, reg_c , "Output:" , out_value )

    # division adv
    if opcode == 0:
        reg_a = reg_a * (2 ** get_operand_value(operand) )

    # out command
    if opcode == 5:

        output_index_move = 1

        if operand == 4:
            reg_a += out_value
        elif operand == 5:
            reg_b += out_value
        elif operand == 6:
            reg_c += out_value

    return reg_a, reg_b , reg_c, output_index_move

def run_reverse_application():
    commands = [(programs[i], programs[i + 1]) for i in range(0, len(programs), 2)]

    pointer = len(commands) - 1
    output_pointer = len(programs) - 1

    while True:
        opcode = commands[pointer][0]
        operand = commands[pointer][1]

        registers["A"] , registers["B"] , registers["C"] , output_move = run_reverse_command (opcode , operand , programs[output_pointer] , registers["A"] , registers["B"] , registers["C"] )

        if output_move > 0:
            output_pointer -= output_move

        pointer -= 1

        # move to last jump
        if pointer < 0:
            for i in range(len(commands)):
                if commands[i][0] == 3:
                    pointer = i
                    break

        if output_pointer < -1:
            break

run_reverse_application()
print(registers)