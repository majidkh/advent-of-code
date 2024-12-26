import re
f = open("inputs/3.txt", "r")
data = f.read()
f.close()

instructions = re.finditer("mul\(\d+,\d+\)|don't\(\)|do\(\)", data)

total1 = total2 = 0

enabled = True
for instruction in instructions:
    command = instruction.group()

    if command.startswith("mul"):
        digits = re.findall("\d+", command)
        total1 += int(digits[0]) * int(digits[1])

        if enabled: total2 += int(digits[0]) * int(digits[1])

    if command.startswith("do()"): enabled = True
    if command.startswith("don't()"): enabled = False

print(total1)
print(total2)