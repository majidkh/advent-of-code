import re

f = open('inputs/18.txt', 'r')
lines = f.read().splitlines()
f.close()

instructions = []
instructions2 = []
num_dirs = {"0":"R","1":"D","2":"L", "3":"U"}
dirs = {"R": (1, 0), "D": (0, 1), "L": (-1, 0), "U": (0, -1)}

for line in lines:
    data = re.findall(r'(\w+) (\d+) \(#([0-9a-z]+)\)', line)
    instructions.append( (data[0][0], int(data[0][1])) )
    instructions2.append( (num_dirs[data[0][2][-1]], int(data[0][2][:-1],16)) )

def shoelace_area(points):
    n = len(points)
    area = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return int(abs(area) / 2)

def calculate( input_ ):
    x,y = (0,0)
    border = 0
    plans = [ (x,y)]
    for instruction in input_:
        direction, length = instruction
        d = dirs[direction]
        x +=  d[0] * length
        y +=  d[1] * length
        border += length
        plans.append( (x, y) )
    area = shoelace_area(plans)
    inside = area - border // 2 + 1
    return inside+border

print("Part 1:", calculate(instructions))
print("Part 2:", calculate(instructions2))