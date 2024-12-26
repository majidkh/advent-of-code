import re
from functools import reduce
from operator import mul
f = open("inputs/14.txt", "r")
lines = f.read().splitlines()
f.close()

# Size of the room
width = 101
height = 103

# List of robots
robots = []

# Robot map to count how many robots are in each cell
grid = [[0 for _ in range(height)] for _ in range(width)]


def teleport (robot_ , robot_map ):

    robot_map[robot_[0]][robot_[1]] -= 1

    robot_[0] += robot_[2]
    robot_[1] += robot_[3]

    if robot_[0] >= width:
        robot_[0] = robot_[0] - width

    elif robot_[0] < 0:
        robot_[0] = width + robot_[0]

    if robot_[1] >= height:
        robot_[1] = robot_[1] - height
    elif robot_[1] < 0:
        robot_[1] = height + robot_[1]

    robot_map[robot_[0]][robot_[1]] += 1

# Detect a line of length characters from the middle point of "mx" and in the "my" Y axis
def detect_line ( mx , my , length , robot_map ):

    for x in range ( mx - length , mx + length  + 1 ):

        if x < 0 or x >= width:
            return False

        if my + length >= height:
            return False

        if robot_map[x][my + length] == 0:

            return False

    return True

# Detect a pyramid shape in the robots in the robot map
def detect_tree ( robots_ , robot_map ):

    for r in robots_:

        x = r[1]
        y = r[0]

        if robot_map[y][x] > 0 :

            # search for 4 rows in a pyramid shape
            found = True
            for l in range(4):
                if not detect_line(y , x , l , robot_map ):
                    found = False
                    break

            if found:
                return True


def print_locations( robot_map ):

    output = ""

    for i in range(height):
        for j in range(width):

            if grid[j][i] != 0:
                output += str(robot_map[j][i])
            else:
                output += "."

        output += "\n"

    print(output)

# Count how many robots are in each quadrant
def count_quadrant( robots_ ):

    quadrants = [0,0,0,0]

    mx = width // 2
    my = height // 2

    for r in robots_:

        if r[0] < mx and r[1] < my:
            quadrants[0] += 1
        elif r[0] > mx and r[1] < my:
            quadrants[1] += 1
        elif r[0] < mx and r[1] > my:
            quadrants[2] += 1
        elif r[0] > mx and r[1] > my:
            quadrants[3] += 1

    return reduce(mul, quadrants)


# create robots and fill the initial robots map
for line in lines:
    px,py,vx,vy = list(map(int,re.findall(r"-?\d+", line)))
    robots.append([px,py,vx,vy])
    grid[px][py] += 1

# Logic
seconds = 0
while True:

    seconds += 1

    for robot in robots:
        teleport( robot , grid )

    # Part 1
    if seconds == 100:
        print("part 1: ", count_quadrant(robots))

    # Part 2
    if detect_tree( robots , grid ):
        print("part 2: ", seconds)
        break

# Bonus ( Print the Christmas tree )
# print_locations(grid)