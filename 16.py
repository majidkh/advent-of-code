import sys,functools,copy
f = open("inputs/16.txt", "r")
lines = f.read().splitlines()
f.close()
sys.setrecursionlimit(100000)
grid = [list(list(line)) for line in lines]
grid2 = copy.deepcopy(grid)

width = len(grid[0])
height = len(grid)
directions = [ (1, 0) , (0, 1), (-1, 0), (0, -1) ] # Left Up Right Down
direction = directions[0]

def print_map( map_ ):

    output = ""

    for i in range(width):
        for j in range(height):

            output += f"{str(map_[i][j]):4}"

        output += "\n"

    print(output)

def get_item( location ):
    x,y = location

    if 0 <= x < width and 0 <= y < height:
        return grid[y][x]

    return None

def move_cursor ( old , new ):
    grid[old[1]][old[0]] = "."
    grid[new[1]][new[0]] = "S"

def find_symbol( symbol ):

    for i in range(width):
        for j in range(height):
            if get_item( (i,j) ) == symbol:
                return i, j

    return None, None

def rotate ( dir_ , degree ):

    if degree == 90:
        index = directions.index(dir_) + 1
        if index >= len(directions):
            index = 0

        return directions[index]

    if degree == -90:
        index = directions.index(dir_) -+ 1
        if index < 0:
            index = len(directions) - 1
        return directions[index]

    return None

def get_neighbours( cursor ):

    neighbours = []

    for i in directions:
        if 0 <= cursor[0] + i[0] < width and 0 <= cursor[1] + i[1] < height:
            neighbours.append( (cursor[0] + i[0], cursor[1] + i[1]) )

    return neighbours

def get_direction ( prev_pos , next_pos ):

    if prev_pos[0] < next_pos[0]:
        return directions[0]
    elif prev_pos[0] > next_pos[0]:
        return directions[2]
    elif prev_pos[1] < next_pos[1]:
        return directions[1]
    elif prev_pos[1] > next_pos[1]:
        return directions[3]

start_pos = find_symbol('S')
end_pos = find_symbol('E')

best_path = {}

# Part 1
def find_path ( cursor , end , current_dir , cost , min_cost ):

    if cursor == end:
        return cost

    state = (cursor[0] , cursor[1] )
    if state in best_path and best_path[state] <= cost:
        return None

    best_path[state] = cost

    neighbours = get_neighbours( cursor )
    for n in neighbours:
        item = get_item(n)

        if item == "#":
            continue

        if item in [".","E"]:

            # Calculate the cost
            new_dir = get_direction(cursor,n)

            addition = 1

            if new_dir != current_dir:
                addition += 1000

            c = find_path( n  , end  , new_dir, cost + addition , min_cost )
            if c is not None and c < min_cost:
                min_cost = c

    return min_cost

result = find_path( start_pos , end_pos , direction,  0 , float("inf")  )
print(result)
