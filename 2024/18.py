from collections import deque
f = open("inputs/18.txt", "r")
lines = f.read().splitlines()
f.close()

width = 71 # Add one extra
height = 71

end_pos = (width - 1 , height-1)

coords = [list(map(int,line.split(","))) for line in lines]


def find_path( length ):

    grid = [[0 for i in range(width)] for j in range(height)]
    for x, y in coords[:length]:
        grid[y][x] = -1

    path = deque([(0,0,0)]) # Start Position
    path_cache = {(0,0)}

    while path:
        col,row,distance = path.popleft()

        for i in [ (1,0) , (-1,0), (0,1), (0,-1) ]:
            x, y = ( col + i[0], row + i[1] )

            if x < 0 or x >= width or y < 0 or y >= height: continue

            if grid[y][x] == -1: continue

            if (x,y) in path_cache: continue

            if (x,y) == end_pos:
                return distance +1

            path_cache.add((x,y))
            path.append( (x,y , distance + 1) )

    return None

print("Part 1:" , find_path(1024))

for i in range( 1024, len(coords) ):
    if find_path( i ) is None:
        print("Part 2:" , f"{coords[i-1][0]},{coords[i-1][1]}" )
        break
