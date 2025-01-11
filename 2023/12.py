from functools import cache

f = open("inputs/12.txt", "r")
lines = f.read().splitlines()
f.close()

records = []
for line in lines:
    s = line.split(" ")[0]
    g = tuple(map(int, line.split(" ")[1].split(",")))
    records.append((s, g))


@cache
def get_arrangements(springs, groups):
    if len(groups) == 0:
        if "#" in springs:
            return 0
        else:
            return 1

    count = 0
    group = groups[0]
    spring_length = 0
    spring_seen = False
    for i in range(len(springs)):

        spring = springs[i]

        next_spring = None
        if i < len(springs) - 1:
            next_spring = springs[i + 1]

        prev_spring = None
        if i >= group:
            prev_spring = springs[i - group]
            if prev_spring == "#": break

        if spring == "#":
            spring_length += 1
            spring_seen = True

        if spring == "?": spring_length += 1

        if spring == ".":
            spring_length = 0
            if spring_seen:
                break
        if spring_length >= group:

            current_spring = springs[i + 1 - group:i + 1]
            if next_spring == "#": continue
            if prev_spring == "#": continue

            count += get_arrangements(springs[i + 2:], groups[1:])
            if current_spring[0] == "#":
                break

    return count


part1 = 0
for s, g in records:
    part1 += get_arrangements(s, g)
print("Part1: ", part1)

part2 = 0
for s, g in records:
    part2 += get_arrangements("?".join([s] * 5), g * 5)
print("Part2: ", part2)