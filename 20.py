from collections import deque
from functools import cache

f = open("inputs/20.txt", "r")
lines = f.read().splitlines()
f.close()
track = [list(list(line)) for line in lines]
width = len(track[0]) # Add one extra
height = len(track)
cheats = []

def get_cell ( col , row ):
    if col < 0 or col >= width or row < 0 or row >= height:
        return None
    return track[row][col]

def is_valid_cheat ( col ,row ):
    if track[row][col] == "#":
        n = 0
        for neighbor in [(1,0) , (-1, 0) , (0,1) , (0,-1)]:
            if get_cell( col + neighbor[0], row + neighbor[1] ) == ".":
                n += 2

        if n >= 2:
            return True

    return False

for cy in range( 1 , height - 1):
    for cx in range(width):
        if is_valid_cheat ( cx , cy):
            cheats.append((cx,cy))

def find_symbol( symbol ):

    for col in range(width):
        for row in range(height):
            if track[row][col] == symbol:
                return col, row

    return None, None

start = find_symbol("S")
end = find_symbol("E")

@cache
def find_path():

    path = deque([( start[0],start[1],0)]) # Start Position
    path_cache = {(0,0)}

    while path:
        col,row,distance = path.popleft()

        for i in [ (1,0) , (-1,0), (0,1), (0,-1) ]:
            x, y = ( col + i[0], row + i[1] )

            if x < 0 or x >= width or y < 0 or y >= height: continue

            if track[y][x] == "#": continue

            if (x,y) in path_cache: continue

            if (x,y) == end:
                return distance +1

            path_cache.add((x,y))
            path.append( (x,y , distance + 1) )

    return None

track_time = find_path()
print(track_time)
