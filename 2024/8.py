import copy
f = open("inputs/8.txt", "r")
data = f.read().splitlines()
f.close()
lines = [list(line) for line in data]
grid_map = copy.deepcopy( lines )

width = len(lines[0])
height = len(lines)

def find_pairs ( character, x , y ):

    found_pairs = []
    for j in range( height ):
        for i in range( width ):
            if x != i and y != j and lines[j][i] == character:
                found_pairs.append( [i,j])

    return found_pairs

def find_antennas ():

    found_pairs = []
    for j in range( height ):
        for i in range( width ):
            if grid_map[j][i] == "#":
                found_pairs.append( [i,j])

    return found_pairs

def add_anti_nodes (antenna_a, antenna_b , follow ):

    distance_x = abs(antenna_a[0] - antenna_b[0])
    distance_y = abs(antenna_a[1] - antenna_b[1])

    if antenna_a[0] < antenna_b[0]:
        x1 = antenna_a[0] - distance_x
        x2 = antenna_b[0] + distance_x
    else:
        x1 = antenna_a[0] + distance_x
        x2 = antenna_b[0] - distance_x

    if antenna_a[1] < antenna_b[1]:
        y1 = antenna_a[1] - distance_y
        y2 = antenna_b[1] + distance_y
    else:
        y1 = antenna_a[1] + distance_y
        y2 = antenna_b[1] - distance_y

    if 0 <= x1 < width and 0 <= y1 < height:
        grid_map[y1][x1] = "#"

    if 0 <= x2 < width and 0 <= y2 < height:
        grid_map[y2][x2] = "#"

    if follow:

        grid_map[antenna_a[1]][antenna_a[0]] = "#"
        grid_map[antenna_b[1]][antenna_b[0]] = "#"

        start = [x1, y1]
        direction = [antenna_a[0] - antenna_b[0], antenna_a[1] - antenna_b[1]]

        while True:
            pos = [ start[0] + direction[0], start[1] + direction[1] ]
            if 0 <= pos[0] < width and 0 <= pos[1] < height:
                grid_map[pos[1]][pos[0]] = "#"

                start = pos
            else:
                break

def pretty_print ( input_grid ):
    for l in input_grid:
        print(l)

def count_antennas():
    count = 0

    for line in grid_map:
        for chars in line:
            if chars == "#":
                count += 1

    return count

def part1():
    for row in range(height):
        line = lines[row]
        for col in range( width ):
            char = line[col]
            if char.isdigit() or char.islower() or char.isupper():
                pairs = find_pairs(char , col, row )

                for pair in pairs:
                    add_anti_nodes( [ col , row ] , pair , False )
    return count_antennas()

print(part1())

# Part 2
def part2():
    for row in range(height):
        line = lines[row]
        for col in range(width):
            char = line[col]
            if char.isdigit() or char.islower() or char.isupper():
                pairs = find_pairs(char, col, row)

                for pair in pairs:
                    add_anti_nodes([col, row], pair , True )
    return count_antennas()


print(part2())
