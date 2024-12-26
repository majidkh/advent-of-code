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

def mark_path ( input_map , start ):

    output = [[-1 for _ in range(height)] for _ in range(width)]
    seen = set()
    output [start[1]] [start[0]] = 0
    seen.add(start)
    queue = deque([start])
    while queue:
        x,y = queue.popleft()
        for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:

            if nx < 0 or nx >= width or ny < 0 or ny >= height: continue
            if (nx,ny) in seen: continue

            if input_map[ny][nx] == "." or input_map[ny][nx] == "E":
                output[ny][nx] = output[y][x] + 1
                seen.add((nx,ny))
                queue.append((nx,ny))
    return output

def find_cheats( radius , savings ):

    cheats = 0
    seen = set()

    for col in range(width):
        for row in range(height):
            if distance_map[row][col] == -1: continue

            for dx in range(-radius, radius + 1):
                for dy in range(-radius, radius + 1):
                    if abs(dx) + abs(dy) <= radius:
                        nx = col + dx
                        ny = row + dy

                        if (nx,ny) in seen: continue
                        if nx < 0 or nx >= width or ny < 0 or ny >= height: continue
                        if distance_map[ny][nx] == -1: continue
                        margin = abs(col - nx ) + abs(row - ny)

                        jump = distance_map[row][col] - distance_map[ny][nx] - margin

                        if jump >= savings :
                            cheats += 1
    return cheats

distance_map = mark_path( track, start )
print ("part 1:", find_cheats(2 , 100 ) )
print ("part 2:", find_cheats(20 , 100 ) )
