f = open("inputs/13.txt", "r")
blocks = f.read().split("\n\n")
f.close()


def check_mirror(grid):
    for row in range(0, len(lines) - 1):
        offset = 0
        mirror = True
        while True:
            if row - offset < 0 or row + 1 + offset >= len(lines):  break
            if grid[row - offset] != grid[row + 1 + offset]: mirror = False
            offset += 1
        if mirror: return (row + 1) * 100

    for col in range(0, len(lines[0]) - 1):
        offset = 0
        mirror = True
        while True:
            if col - offset < 0 or col + 1 + offset >= len(lines[0]):  break
            for row in range(len(lines)):
                if grid[row][col - offset] != grid[row][col + 1 + offset]: mirror = False
            offset += 1
        if mirror: return col + 1

    return 0


part1 = 0
for block in blocks:
    lines = block.split("\n")

    val = check_mirror(lines)
    part1 += val

print("Part 1:", part1)
