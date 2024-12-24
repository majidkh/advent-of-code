import re
f = open("inputs/24.txt", "r")
lines = f.read()
f.close()

inputs = {}
outputs = {}
commands = []

for line in lines:
    value = re.findall("(\w+): (\d+)", lines)
    for v in value:
        inputs[v[0]] = int(v[1])

values = re.findall("(\w+) (\w+) (\w+) -> (\w+)", lines)
for v in values:
    commands.append([ v[0], v[1], v[2], v[3] , False ])

for c in commands:
    if c[0] not in inputs:
        inputs[c[0]] = None
    if c[2] not in inputs:
        inputs[c[2]] = None

def calculate( input_command ):

    v1 = inputs[input_command[0]]
    v2 = inputs[input_command[2]]
    operator = input_command[1]

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

def is_command_ready ( input_command ):
    v1 = inputs[input_command[0]]
    v2 = inputs[input_command[2]]

    if v1 is None or v2 is None:
        return False

    return True

while True:

    all_done = True
    for i in range(len(commands)):
        command = commands[i]

        if is_command_ready(command):

            r = calculate( command )

            if command[3] not in inputs or inputs[command[3]] is None:
                inputs[command[3]] = r
            if command[3] not in outputs:
                outputs[command[3]] = r

            commands[i][4] = True

        if not commands[i][4]:
            all_done = False
    if all_done:
        break


sorted_dict = {key: value for key, value in sorted(outputs.items())}

output = ""
for key, value in sorted_dict.items():
    if key.startswith("z"):
        output += str(value)

print(int(output[::-1],2))
