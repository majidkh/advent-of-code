from collections import deque
from functools import cache
import copy

f = open("inputs/20.txt", "r")
lines = f.read().splitlines()
f.close()
track = tuple(tuple(tuple(line)) for line in lines)
width = len(track[0]) # Add one extra
height = len(track)
cheats = []

def get_cell ( col , row ):
    if col < 0 or col >= width or row < 0 or row >= height:
        return None
    return track[row][col]

for cy in range( 1 , height - 1):
    for cx in range(width):
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
def find_path( cheat , cheat_length ):

    path = deque([( start[0],start[1],0)]) # Start Position
    path_cache = {(0,0)}

    while path:
        col,row,distance = path.popleft()

        for i in [ (1,0) , (-1,0), (0,1), (0,-1) ]:
            x, y = ( col + i[0], row + i[1] )

            if x < 0 or x >= width or y < 0 or y >= height: continue

            if track[y][x] == "#":

                # Check cheat
                if cheat_length == 1 and cheat != (x,y): continue
                if cheat_length == 20:
                    

            if (x,y) in path_cache: continue

            if (x,y) == end:
                return distance +1

            path_cache.add((x,y))
            path.append( (x,y , distance + 1) )

    return None

normal_time = find_path( (-1,-1) , 1 )


part1 = 0
print(len(cheats))
for i in range(len(cheats)):
    if i % 100 == 0:
        print(i)
    c = cheats[i]
    result = find_path( c , 20 )
    if result is not None and result < normal_time:
        if normal_time  - result >= 100:
            part1 += 1

print("Part 1:", part1)