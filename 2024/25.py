from itertools import combinations

f = open("inputs/25.txt", "r")
lines = f.read()
f.close()

keys = []
locks = []

for schematics in lines.split("\n\n"):

    schematic = schematics.split("\n")
    pins = [-1] * len(schematic[0])

    if schematic[0].startswith("#"):
        for i in range(len(schematic)):
            for c in range(len(schematic[i])):
                if schematic[i][c] == "#":
                    pins[c] += 1
        locks.append(pins)
    else:
        for i in range(len(schematic)):
            for c in range(len(schematic[i])):
                if schematic[i][c] == "#":
                    pins[c] += 1

        keys.append(pins)


def is_fit ( key , lock ):
    for i in range(len(key)):
        if key[i] + lock[i] > 5:
            return False

    return True

part1 = 0
for lock in locks:
    for key in keys:
        if is_fit(key, lock):
            part1 += 1

print("Part 1:", part1)
