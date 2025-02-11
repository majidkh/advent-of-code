from collections import deque

f = open ("inputs/21.txt", "r")
lines = f.read().splitlines()
f.close()

grid = [list(line) for line in lines]
width = len(grid[0])
height = len(grid)

def get_cell ( col , row ):
    if col < 0 or col >= width or row < 0 or row >= height:
        return None
    return grid[row][col]

def find_symbol( symbol ):
    for col in range(width):
        for row in range(height):
            if grid[row][col] == symbol:
                return col, row
    return None, None

def simulate( start , steps ):

    path = deque()
    plots = set()
    plots.add(start)
    path.append( plots )

    while steps > 0 and path:
        spots = path.popleft()
        plots = set()

        for spot in spots:
            for n in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny = n[0] + spot[0], n[1] + spot[1]

                if get_cell( nx,ny) in ".S":
                    plots.add((nx,ny))

        if len(plots) > 0:
            path.append(plots)
        steps -= 1

    return len(path[0])

print("Part 1:", simulate( find_symbol("S"), 64))
