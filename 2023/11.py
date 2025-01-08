from itertools import combinations

f = open('inputs/11.txt', 'r')
lines = f.read().splitlines()
f.close()

grid = []
for line in lines: grid.append(list(line))

galaxies = []
for j in range(len(grid)):
    for i in range(len(grid[0])):
        if grid[j][i] == "#":
            galaxies.append((i, j))

pairs = list(combinations(galaxies, 2))
part1 = part2 = 0

empty_rows = set()
for j in range(len(grid)):
    if all(col == "." for col in grid[j]):
        empty_rows.add(j)

empty_cols = set()
for i in range(len(grid[0])):
    if all(row[i] == "." for row in grid):
        empty_cols.add(i)

for pair in pairs:

    pair1, pair2 = pair
    empty = steps = 0

    distance = 0
    for i in range(min(pair1[0], pair2[0]), max(pair1[0], pair2[0])):
        if i in empty_cols:
            empty += 1
        else:
            steps += 1

    for j in range(min(pair1[1], pair2[1]), max(pair1[1], pair2[1])):
        if j in empty_rows:
            empty += 1
        else:
            steps += 1

    part1 += steps + empty * 2
    part2 += steps + (empty * 1000000)

print("Part 1:", part1)
print("Part 2:", part2)
