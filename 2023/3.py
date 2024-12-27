import re

f = open("inputs/3.txt", "r")
lines = f.read().splitlines()
f.close()

p = re.compile("(\d+)")
s = re.compile(r'[^a-zA-Z0-9.]')

digits = []
symbols = []

for i in (range(len(lines))):
    line = lines[i]

    for digit in p.finditer(line):
        # left, top, right, bottom
        rect = [digit.start() - 1, i - 1, digit.end(), i + 1]
        digits.append([int(digit.group()), rect])

    for symbol in s.finditer(line):
        # x,y
        symbols.append((symbol.group(), symbol.start(), i))

part1 = 0

for number, corners in digits:
    left, top, right, bottom = corners
    for symbol, x, y in symbols:
        if left <= x <= right and top <= y <= bottom:
            break
    else:
        continue

    part1 += number

# Part 2
connections = {}
for symbol, x, y in symbols:
    if symbol == "*":
        for number, corners in digits:
            left, top, right, bottom = corners
            if left <= x <= right and top <= y <= bottom:
                if (x, y) in connections:
                    connections[(x, y)].append(number)
                else:
                    connections[(x, y)] = [number]

part2 = 0
for i in connections:
    if len(connections[i]) == 2:
        part2 += connections[i][0] * connections[i][1]

print("Part 1:", part1)
print("Part 2:", part2)
