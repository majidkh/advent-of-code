import math
import re

f = open('inputs/18.txt', 'r')
lines = f.read().splitlines()
f.close()

instructions = []
instructions2 = []
num_dirs = {"0":"R","1":"D","2":"L", "3":"U"}
dirs = {"R": (1, 0), "D": (0, 1), "L": (-1, 0), "U": (0, -1)}

for line in lines:
    data = re.findall(r'(\w+) (\d+) \(#([0-9a-z]+)\)', line)
    instructions.append( (data[0][0], int(data[0][1])) )
    instructions2.append( (num_dirs[data[0][2][-1]], int(data[0][2][:-1],16)) )


# find minimum x , y so later we can adjust the grid
x, y = 0, 0
min_x = min_y = 0
for instruction in instructions:
    direction, length = instruction
    d = dirs[direction]
    for i in range(length):
        x += d[0]
        y += d[1]
        if x < min_x: min_x = x
        if y < min_y: min_y = y

# Add one row and column margin from left and top for bfs search
min_x -= 1
min_y -= 1

# create the dig plans
plans = set()
x, y = 0, 0
for instruction in instructions:
    direction, length = instruction
    d = dirs[direction]
    for i in range(length):
        x += d[0]
        y += d[1]
        plans.add((x + abs(min_x), y + abs(min_y)))

# add one margin to right and bottom too
max_x = max(pt[0] for pt in plans) + 1
max_y = max(pt[1] for pt in plans) + 1

width = max_x - min_x
height = max_y - min_y

grid = [["." for _ in range(width)] for _ in range(height)]

# Used to caching the below function so we don't search all the cells again
open_list = set()
closed_list = set()

def is_closed(x1, y1):
    global open_list, closed_list

    if (x1, y1) in open_list:
        return False
    elif (x1, y1) in closed_list:
        return True

    if x1 == 0 or x1 == width - 1 or y1 == 0 or y1 == height - 1:
        return False

    q = [(x1, y1)]
    seen = set()

    corners = {(0, 0), (width - 2, 0), (0, height - 2), (width - 2, height - 2)}

    enclosed = True

    while q:
        x1, y1 = q.pop()

        for nx, ny in [(x1 + 1, y1), (x1 - 1, y1), (x1, y1 + 1), (x1, y1 - 1)]:
            if nx < 0 or nx >= width or ny < 0 or ny >= height: continue
            if (nx, ny) in plans: continue

            if (nx, ny) in seen: continue
            seen.add((nx, ny))

            if (nx, ny) in corners:
                enclosed = False

            q.append((nx, ny))

    if not enclosed:
        open_list |= seen
    else:
        closed_list |= seen

    return enclosed


part1 = 0
for j in range(height):
    for i in range(width):
        if (i, j) in plans:
            grid[j][i] = "#"
            part1 += 1
        else:
            # check if this block is within the shape
            if is_closed(i, j):
                grid[j][i] = "#"
                part1 += 1


def pretty_print(g):
    output = ""
    for row in range(height):
        for col in range(width):
            output += str(g[row][col])
        output += "\n"
    print(output)


# pretty_print(grid)

print("Part 1:", part1)
