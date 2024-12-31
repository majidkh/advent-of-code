f = open('inputs/10.txt', 'r')
lines = f.read().splitlines()
f.close()

width = len(lines[0])
height = len(lines)

valid_connections = {
    "F": [(1, 0), (0, 1)],
    "7": [(-1, 0), (0, 1)],
    "L": [(1, 0), (0, -1)],
    "J": [(-1, 0), (0, -1)],
    "|": [(0, -1), (0, 1)],
    "-": [(1, 0), (-1, 0)],
    "S": [(1, 0), (-1, 0), (0, 1), (0, -1)]
}


def find_symbol(symbol):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[j][i] == symbol:
                return i, j


def is_connected(current_pipe, next_pipe):
    x, y = current_pipe
    nx, ny = next_pipe

    current_shape = lines[y][x]
    next_shape = lines[ny][nx]

    if (nx - x, ny - y) not in valid_connections[current_shape]: return False
    if (x - nx, y - ny) not in valid_connections[next_shape]: return False

    return True


def find_loop(sx, sy):
    x, y = sx, sy
    path = []

    steps = 0

    while steps == 0:

        # pick the first pipe
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:

            if nx < 0 or nx >= width or ny < 0 or ny >= height: continue
            if lines[ny][nx] == ".": continue

            if len(path) > 1:
                if (nx, ny) == path[-2]: continue

            if is_connected((x, y), (nx, ny)):

                if nx == sx and ny == sy:
                    steps = (len(path) // 2) + 1

                path.append((nx, ny))
                x, y = nx, ny

                break

    return steps


start = find_symbol('S')
print("Part 1:", find_loop(start[0], start[1]))
