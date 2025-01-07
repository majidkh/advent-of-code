from collections import deque

f = open('inputs/10.txt', 'r')
lines = f.read().splitlines()
f.close()

grid = []
for line in lines:
    grid.append(list(line))
width = len(grid[0])
height = len(grid)

# Find the start Position
sx, sy = [(x, y) for x in range(width) for y in range(height) if grid[y][x] == 'S'][0]

pipe_chars = {"7": "\u2577", "L": "\u2514", "F": "\u250C", "J": "\u2518", "-": "\u2500", "|": "\u2502"}

pipe_connections = {
    "F": [(1, 0), (0, 1)],
    "7": [(-1, 0), (0, 1)],
    "L": [(1, 0), (0, -1)],
    "J": [(-1, 0), (0, -1)],
    "|": [(0, -1), (0, 1)],
    "-": [(1, 0), (-1, 0)]
}


def pretty_print(map_, replace=False):
    output = ""
    for j in range(len(map_)):
        for i in range(len(map_[0])):

            if map_[j][i] in pipe_chars and replace:
                output += pipe_chars[map_[j][i]]
            else:
                output += map_[j][i]
        output += "\n"
    print(output)


# Detect the start pipe shape
def find_pipe(map_, col, row):
    pipe = map_[row][col]

    s_conns = []
    for nx, ny, conn in [(col + 1, row, "-J7"), (col - 1, row, "-LF"), (col, row + 1, "|LJ"), (col, row - 1, "|7F")]:
        if nx < 0 or nx >= width or ny < 0 or ny >= height: continue
        if grid[ny][nx] in conn:
            s_conns.append((nx - col, ny - row))

    if (-1, 0) in s_conns and (0, 1) in s_conns:
        pipe = "7"
    elif (-1, 0) in s_conns and (0, -1) in s_conns:
        pipe = "J"
    elif (1, 0) in s_conns and (0, 1) in s_conns:
        pipe = "F"
    elif (1, 0) in s_conns and (0, 1) in s_conns:
        pipe = "L"
    elif (1, 0) in s_conns and (-1, 0) in s_conns:
        pipe = "-"
    elif (0, 1) in s_conns and (0, -1) in s_conns:
        pipe = "|"

    return pipe


s_pipe = find_pipe(grid, sx, sy)
grid[sy][sx] = s_pipe


def is_connected(map_, current_pipe, next_pipe):
    x, y = current_pipe
    nx, ny = next_pipe
    current_shape = map_[y][x]
    next_shape = map_[ny][nx]
    if (nx - x, ny - y) not in pipe_connections[current_shape]: return False
    if (x - nx, y - ny) not in pipe_connections[next_shape]: return False
    return True


def find_loop(map_, sx, sy):
    path = []

    seen = set()
    blocks = deque()
    blocks.append((sx, sy))

    while blocks:

        x, y = blocks.popleft()
        if (x, y) in seen: continue
        seen.add((x, y))
        # pick the first pipe
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if nx < 0 or nx >= width or ny < 0 or ny >= height: continue
            if map_[ny][nx] == ".": continue
            if (nx, ny) in seen: continue
            if is_connected(map_, (x, y), (nx, ny)):
                path.append((nx, ny))
                blocks.append((nx, ny))
                break

    return path + [(sx, sy)]


loop = find_loop(grid, sx, sy)
print("Part 1:", len(loop) // 2)

# Part 2 Remove unwanted pipes
grid2 = [['.' for _ in range(width)] for _ in range(height)]
for j in range(height):
    for i in range(width):
        if (i, j) in loop:
            grid2[j][i] = grid[j][i]
        else:
            grid2[j][i] = "."


def count_crosses(map_, tile, bend_pipes):
    x, y = tile
    crosses = 0
    last_pipe = ""
    for x in range(x, width):
        if map_[y][x] in ".-": continue
        if last_pipe in bend_pipes and map_[y][x] == bend_pipes[last_pipe]:
            crosses += 1
        elif map_[y][x] == "|":
            crosses += 1

        last_pipe = map_[y][x]

    return crosses


part2 = 0
for j in range(height):
    for i in range(width):
        if grid2[j][i] != ".": continue
        c1 = count_crosses(grid2, (i, j), {"F": "J", "L": "7"})
        if c1 % 2 == 1:
            part2 += 1

print("Part 2:", part2)

# pretty_print(grid2 , True )