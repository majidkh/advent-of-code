from collections import deque

f = open("inputs/20.txt", "r")
lines = f.read().splitlines()
f.close()
track = [list(line) for line in lines]
width = len(track[0])
height = len(track)
distances = {}

def get_cell ( input_map, col , row ):
    if col < 0 or col >= width or row < 0 or row >= height:
        return None
    return input_map[row][col]

def find_symbol( symbol ):
    for col in range(width):
        for row in range(height):
            if track[row][col] == symbol:
                return col, row
    return None, None

def pretty_print( input_map ):
    output = ""
    for i in range(width):
        for j in range(height):
            output += str(input_map[i][j]).center(4 , " ")
        output += "\033[0m\n"
    print(output)

start = find_symbol("S")
end = find_symbol("E")

def mark_path ( input_map , end ):

    output = [[-1 for _ in range(height)] for _ in range(width)]

    output[end[1]][end[0]] = 0

    seen = set()
    seen.add(end)
    queue = deque([end])
    while queue:
        x,y = queue.popleft()
        for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:

            if nx < 0 or nx >= width or ny < 0 or ny >= height: continue

            if (nx,ny) in seen: continue

            if input_map[ny][nx] == "." or input_map[ny][nx] == "S":
                output[ny][nx] = output[y][x] + 1
                seen.add((nx,ny))
                queue.append((nx,ny))
    return output

def is_shortcuts ( input_map , x , y , target_distance, radius ):
    values = []
    for nx, ny in [( x + 1, y ), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if nx < 0 or nx >= width or ny < 0 or ny >= height: continue
        value = get_cell(input_map, nx, ny)
        if value > -1:
            values.append ( value )

    if len(values) > 1:
        if max(values) - min(values) > target_distance:
            return True

    return False

def find_cheats ( input_map , time_save , radius = 1 ):
    cheats = 0
    for col in range(width):
        for row in range(height):
            if input_map[row][col] == -1:
                if is_shortcuts( input_map, col, row, time_save + 1, radius):
                    cheats += 1
    return cheats

distance_map = mark_path( track, end )
print ( "Part 1:", find_cheats( distance_map  ,100 , 1 ))
