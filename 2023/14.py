f = open("inputs/14.txt", "r")
grid = list(list(g for g in line) for line in f.read().splitlines())
f.close()

height = len(grid)
width = len(grid[0])


def can_move_to(map_, rock_, dir_):
    if rock_[1] + dir_[1] < 0 or rock_[1] + dir_[1] >= height: return False
    if rock_[0] + dir_[0] < 0 or rock_[0] + dir_[0] >= width: return False
    if map_[rock_[1] + dir_[1]][rock_[0] + dir_[0]] == ".":
        return True
    return False


def pretty_print(map_):
    output = ""
    for row in range(len(map_)):
        for col in range(len(map_[row])):
            output += map_[row][col]
        output += "\n"

    print(output)


def tilt(map_, dir_):
    while True:
        can_move = False

        for row in range(len(map_)):
            for col in range(len(map_[row])):

                if map_[row][col] == "O":
                    if can_move_to(map_, (col, row), dir_):
                        map_[row][col] = "."
                        map_[row + dir_[1]][col + dir_[0]] = "O"
                        can_move = True

        if not can_move:
            break


def calculate_load(map_):
    load = 0
    for row in range(len(map_)):
        for col in range(len(map_[row])):
            if map_[row][col] == "O":
                load += len(map_) - row

    return load


tilt(grid, (0, -1))
print("Part 1:", calculate_load(grid))

g = tuple(tuple(inner_list) for inner_list in grid)
seen = {g}
grids = [g]
loop = 0

while True:
    loop += 1

    for direction in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        tilt(grid, direction)
        g = tuple(tuple(inner_list) for inner_list in grid)

    if g not in seen:
        seen.add(g)
        grids.append(g)
    else:
        break

first = grids.index(g)

index = ((1000000000 - first) % (loop - first)) + first
print("Part 2:", calculate_load(grids[index]))
