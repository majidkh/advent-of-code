import copy
f = open("inputs/6.txt", "r")
data = f.read().splitlines()
f.close()
lines = [list(line) for line in data]

def find_guard( input_grid ):

    for row in range(len(input_grid)):
        for col in range(len(input_grid[row])):

            if input_grid[row][col] == "^":
                return [col, row], [0, -1], "^"

            if input_grid[row][col] == ">":
                return [col, row], [1 , 0], ">"

            if input_grid[row][col] == "<":
                return [col, row], [-1 , 0], "<"

            if input_grid[row][col] == "v":
                return [col, row], [0 , 1], "v"

    return None, [0,0],""

def get_block( input_grid, pos ):
    # Check for x Bounds
    if pos[0] < 0 or pos[0] >= len(input_grid[0]):
        return None

    if pos[1] < 0 or pos[1] >= len(input_grid):
        return None

    return input_grid[pos[1]][pos[0]]

def replace_symbol ( input_grid , pos , symbol ):
    input_grid [ pos[1]] [ pos[0]] = symbol

def rotate( symbol ):

    if symbol == "^":
        return [1, 0], ">"
    if symbol == ">":
        return [0, 1], "v"
    if symbol == "v":
        return [-1, 0], "<",
    if symbol == "<":
        return [0, -1], "^"

def get_steps( input_grid):

    result = []

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if input_grid[y][x] == "X":
                result.append([x, y])

    return result

def pretty_print ( input_grid ):
    for line in input_grid:
        print(line)


def travel ( input_grid , g_pos , g_dir, g_icon  ):

    path = {}

    while True:


        next_pos = [g_pos[0] + g_dir[0], g_pos[1] + g_dir[1]]
        front_block = get_block(input_grid, next_pos)

        key = str(next_pos[0]) + "_" + str(next_pos[1]) + "_" + str(g_dir[0]) + "_" + str(g_dir[1])


        # Check to see if guard has been here before?
        if key in path.keys():
            return True

        path[key] = 1

        if front_block in [".", "X"]:

            replace_symbol(input_grid, g_pos, "X")
            replace_symbol(input_grid, next_pos, g_icon)

            g_pos = next_pos


        # Rotate 90 degrees
        if front_block == "#":
            g_dir, g_icon = rotate(g_icon)

        if front_block is None:
            replace_symbol(input_grid, g_pos, "X")
            return False

# Part 1
grid1 = copy.deepcopy( lines )
guard,direction,icon = find_guard( grid1 )

loop = travel ( grid1 , guard , direction, icon )

steps = get_steps( grid1 )
print(len(steps))


# Part 2
obstacle_count = 0
for step in steps[1:]:

    grid2 = copy.deepcopy( lines )

    guard, direction, icon = find_guard(grid2)

    if guard is None:
       continue

    if step == guard:
       continue

    replace_symbol(grid2, step, "#")

    if travel(grid2, guard, direction, icon  ):
        obstacle_count += 1

print ( obstacle_count)