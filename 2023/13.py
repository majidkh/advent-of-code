f = open("inputs/13.txt", "r")
blocks = f.read().split("\n\n")
f.close()


def check_mirror(grid, find_smudge=False):
    for row in range(0, len(lines) - 1):
        offset = 0
        mirror = True
        smudges = []
        while True:
            if row - offset < 0 or row + 1 + offset >= len(lines):  break

            for col in range(len(lines[row])):
                if grid[row - offset][col] != grid[row + 1 + offset][col]:
                    mirror = False
                    smudges.append([col, row - offset])
            offset += 1

        if find_smudge:
            if len(smudges) == 1:
                return (row + 1) * 100
        elif mirror:
            return (row + 1) * 100

    for col in range(0, len(lines[0]) - 1):
        offset = 0
        mirror = True
        smudges = []
        while True:
            if col - offset < 0 or col + 1 + offset >= len(lines[0]):  break
            for row in range(len(lines)):
                if grid[row][col - offset] != grid[row][col + 1 + offset]:
                    mirror = False
                    smudges.append([col - offset, row])

            offset += 1

        if find_smudge:
            if len(smudges) == 1:
                return col + 1
        elif mirror:
            return col + 1

    return 0


part1 = 0
part2 = 0
for block in blocks:
    lines = block.split("\n")
    part1 += check_mirror(lines, False)
    part2 += check_mirror(lines, True)

print("Part 1:", part1)
print("Part 2:", part2)
