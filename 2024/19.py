from functools import cache

f = open("inputs/19.txt", "r")
lines = f.read().split("\n\n")
f.close()
patterns = lines[0].strip().split(",")
patterns = [pattern.strip() for pattern in patterns]

designs = lines[1].strip().split("\n")

@cache
def is_possible ( design_  ):
    if design_ == "":
        return 1

    count = 0
    for p in patterns:
        if design_.startswith(p):
            count += is_possible ( design_[len(p):] )

    return count

part1 = 0
part2 = 0
for design in designs:
    options = is_possible( design )

    if options > 0:
        part1 += 1

    part2 += options

print("Part 1:", part1)
print("Part 2:", part2)
