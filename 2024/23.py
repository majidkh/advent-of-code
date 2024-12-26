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

groups = []
for s in sets:
    groups.append( make_unique(s) )

max_length = 0
max_group = []
for pc1,pc2 in connections:
    for i in range(len(groups)):
        group = groups[i]
        if pc1 in group and pc2 in group: continue # already exists
        if pc1 not in group and pc2 not in group: continue # none exists

        if pc2 in group:
            a = pc1
            pc1 = pc2
            pc2 = a

        # Pc 1 is already there, check if pc2 has connection to the rest of the group
        if set(group).issubset(network[pc2]):
            groups[i] =  make_unique( group + tuple([pc2]) )

            if len(groups[i]) > max_length:
                max_length = len(groups[i])
                max_group = groups[i]


print("Part 2:", ",".join(make_unique(max_group)))