import re
from math import gcd
from functools import reduce

f = open('inputs/8.txt', 'r')
lines = f.read().splitlines()
f.close()

instruction = lines[0]
nodes = {}
for line in lines[2:]:
    m = re.findall(r'(\w+) = \((\w+), (\w+)\)', line)[0]
    if len(m) == 3:
        nodes[m[0]] = (m[1], m[2])

current = "AAA"
end = "ZZZ"
index = 0
loop = 0

while current != end:

    direction = instruction[index]
    if direction == "L":
        current = nodes[current][0]

    elif direction == "R":
        current = nodes[current][1]

    index += 1
    if index >= len(instruction):
        index = 0

    loop += 1

print("Part 1:", loop)

# Part 2

ghosts = []
for node in nodes.keys():
    if node.endswith("A"):
        ghosts.append([node, 0])

index = 0
loop = 1

# Calculate steps take for each element to land on ending Z for the first time
while True:
    direction = instruction[index]
    if direction == "L":
        for i in range(len(ghosts)):
            ghosts[i][0] = nodes[ghosts[i][0]][0]
            if ghosts[i][0].endswith("Z"):
                ghosts[i][1] = loop

    elif direction == "R":
        for i in range(len(ghosts)):
            ghosts[i][0] = nodes[ghosts[i][0]][1]
            if ghosts[i][0].endswith("Z"):
                ghosts[i][1] = loop

    index += 1
    if index >= len(instruction):
        index = 0
    loop += 1

    arrived = True
    for ghost in ghosts:
        if not ghost[0].endswith("Z") and ghost[1] == 0:
            arrived = False

    if arrived:
        break


# Now Calculate the lowest common multiple
def lcm(a, b):
    return a * b // gcd(a, b)


steps = reduce(lcm, [ghost[1] for ghost in ghosts])
print("Part 2:", steps)
