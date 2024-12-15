import copy
f = open("inputs/15.txt", "r")
data = f.read().split("\n\n")
f.close()

grid_map = []
grid_map2 = []
moves = []

for line in data[0].split("\n"):
    grid_map.append(list(line))

    row = []
    for item in line:
        if item == "#":
            row.append("#")
            row.append("#")
        elif item == "O":
            row.append("[")
            row.append("]")
        elif item == "@":
            row.append("@")
            row.append(".")
        elif item == ".":
            row.append(".")
            row.append(".")


    grid_map2.append(row)

for line in data[1].split("\n"):
    for unit in line:
        moves.append(unit)

def get_item ( x , y ):

    if 0 <= x < len(grid_map[0]) and 0 <= y < len(grid_map):
        return grid_map[y][x]

    return None

def find_robot():
    for y in range( len(grid_map) ):
        for x in range( len(grid_map[0]) ):
            if get_item(x,y) == "@":
                return x, y

    return None, None


def can_move ( x , y , vx , vy ):

    block = get_item(x, y)

    if block == ".":
        return True

    if block == "#":
        return False

    if block == "O":
        return can_move ( x + vx, y + vy , vx , vy )

    if vy == 1 or vy == -1:
        if block == "[":
            return can_move ( x + vx , y + vy , vx , vy ) and can_move ( x + vx + 1, y + vy , vx , vy )

        if block == "]":
            return can_move ( x + vx , y + vy , vx , vy ) and can_move ( x + vx - 1, y + vy , vx , vy )

    if block == "[":
        return can_move(x + vx, y + vy, vx, vy)

    if block == "]":
        return True

def push_block ( x , y , vx , vy ):

    if not can_move ( x , y , vx , vy ):
        return False

    block = get_item(x,y)

    if block == ".":
        return True

    # if it's a single box
    if block == "O":
        if push_block (x + vx,y +vy,vx,vy):
            grid_map[y][x] = "."
            grid_map[y + vy][x + vx] = "O"
            return True

    # if it's a big box
    if block == "]":

        # for up and down movements
        if vy == 1 or vy == -1:

            # if both can move up
            if push_block(x + vx, y + vy, vx, vy) and push_block(x - 1 + vx, y + vy, vx, vy):
                grid_map[y][x] = "."
                grid_map[y][x - 1] = "."
                grid_map[y + vy][x + vx] = "]"
                grid_map[y + vy][x - 1 + vx] = "["
                return True

        elif push_block(x + vx, y + vy, vx, vy):
            grid_map[y][x] = "."
            grid_map[y + vy][x + vx] = "]"
            return True

    if block == "[":

        # for up and down movements
        if vy == 1 or vy == -1:

            # if both can move up
            if push_block(x + vx, y + vy, vx, vy) and push_block(x + 1 + vx , y + vy, vx, vy):

                grid_map[y][x] = "."
                grid_map[y][x+1] = "."
                grid_map[y + vy][x + vx] = "["
                grid_map[y + vy][x + 1 + vx ] = "]"
                return True

        elif push_block(x + vx, y + vy, vx, vy):
            grid_map[y][x] = "."
            grid_map[y + vy][x + vx] = "["
            return True

    return False

def move_robot( x , y , symbol ):

    if symbol == "<":
        if push_block( x - 1 , y , -1 , 0 ):
            grid_map[y][x] = "."
            grid_map[y][x-1] = "@"
            return [x - 1 , y]

    if symbol == ">":
        if push_block( x + 1 , y , 1 , 0 ):
            grid_map[y][x] = "."
            grid_map[y][x+1] = "@"
            return [x + 1 , y]

    if symbol == "v":
        if push_block( x , y + 1 , 0 , 1 ):
            grid_map[y][x] = "."
            grid_map[y +1][x] = "@"
            return [x , y + 1]

    if symbol == "^":
        if push_block( x , y - 1 , 0 , -1 ):
            grid_map[y][x] = "."
            grid_map[y -1][x] = "@"
            return [x , y - 1]

    return None

def calculate_gps_coord():

    h = len(grid_map)
    w = len(grid_map[0])

    total = 0
    for y in range( h ):
        for x in range(w):

            if get_item(x,y) == "O":
                total += ( y * 100) + x

            if get_item(x,y) == "[":
                total += y * 100 + x

    return total


robot = find_robot()

for move in moves:
    result = move_robot( robot[0], robot[1], move )
    if result is not None:
        robot = result

print( "part 1:", calculate_gps_coord())

# Part 2
grid_map = grid_map2
robot = find_robot()

for move in moves:
    result = move_robot( robot[0], robot[1], move )
    if result is not None:
        robot = result

print( "part 2:", calculate_gps_coord())
