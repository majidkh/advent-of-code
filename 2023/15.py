f = open("inputs/15.txt", "r")
hashes = f.read().split(",")
f.close()

part1 = 0
for h in hashes:
    v = 0
    for c in h:
        v += ord(c)
        v = (v * 17) % 256
    part1 += v

print("Part 1:", part1)