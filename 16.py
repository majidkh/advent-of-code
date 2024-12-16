import sys,copy

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

def get_neighbours( cursor , current_dir ):

    neighbours = []

    left = rotate(current_dir , - 90)
    right = rotate(current_dir , 90)

    neighbours.append( (cursor[0] + current_dir[0], cursor[1] + current_dir[1]) )
    neighbours.append( (cursor[0] + left[0], cursor[1] + left[1]) )
    neighbours.append( (cursor[0] + right[0], cursor[1] + right[1]) )

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

def get_seat_count (input_map ):
    count = 0
    for i in range(width):
        for j in range(height):
            if input_map[i][j] == "O":
                count += 1
    return count

start_pos = find_symbol('S')
end_pos = find_symbol('E')
best_path = {}

paths = []

# Part 1
def find_path ( cursor , end , current_dir , cost , min_cost , path ):

    if cursor == end:
        if min_cost > 0 or cost < min_cost:
            paths.append( [ cost , path] )
        return cost

    state = (cursor[0] , cursor[1] , current_dir )

    if cost > min_cost > 0:
        return None

    if state in best_path and best_path[state] < cost:
        return None

    best_path[state] = cost

    neighbours = get_neighbours( cursor , current_dir )
    for n in neighbours:
        item = get_item(n)

        if item == "#":
            continue

        if n in path:
            continue

        if item in [".","E"]:

            # Calculate the cost
            new_dir = get_direction(cursor,n)

            addition = 1

            if new_dir != current_dir:
                addition += 1000

            c = find_path( n  , end  , new_dir, cost + addition , min_cost , path + [(n[0],n[1])] )

            if c is not None and c < min_cost:
                min_cost = c

    return min_cost

lowest_score = find_path( start_pos , end_pos , direction,  0 , float("inf") ,   [(start_pos[0] , start_pos[1])]  )
print("part1", lowest_score)

# part 2
for result in paths:
    if result[0] == lowest_score:
        for p in result[1]:
            grid2[p[0]][p[1]] = "O"

print("part 2", get_seat_count(grid2))