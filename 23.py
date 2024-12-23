import re
f = open("inputs/23.txt", "r")
lines = f.read()
f.close()

connections = re.findall("(\w+)-(\w+)", lines)
network = {}

for pc1,pc2 in connections:
    if pc1 not in network: network[pc1] = set()
    network[pc1].add(pc2)
    if pc2 not in network: network[pc2] = set()
    network[pc2].add(pc1)

sets = set()

def make_unique( chain ):
    return tuple(sorted(chain))

# Loop through the unique elements
for pc1 in network:
    for pc2 in network[pc1]:
        for pc3 in network[pc2]:
            if pc1 == pc3: continue
            if not pc1 in network[pc3]: continue
            sets.add( make_unique( [pc1 , pc2 , pc3] ) )

part1 = 0
for item in sets:
    for pc in item:
        if pc.startswith("t"):
            part1 += 1
            break

print("Part 1:" , part1)
