import re

f = open('inputs/8.txt', 'r')
lines = f.read().splitlines()
f.close()

instruction = lines[0]
nodes = {}
for line in lines[2:]:
    m = re.findall(r'(\w+) = \((\w+), (\w+)\)', line)[0]
    nodes[m[0]] = (m[1], m[2])

current = "AAA"
end = "ZZZ"
index = 0
steps = 0

while current != end:

    direction = instruction[index]
    if direction == "L":
        current = nodes[current][0]
    elif direction == "R":
        current = nodes[current][1]

    index += 1
    if index >= len(instruction):
        index = 0
    steps += 1

print("Part 1:", steps)
