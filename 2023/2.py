import re
f = open("inputs/2.txt")
lines = f.read().splitlines()
f.close()

capacity = { "red" : 12 , "green": 13 , "blue": 14 }

part1 = 0
part2 = 0
for line in lines:
    gameId = re.findall(r"Game (\d+):" , line )
    draws = line.split(";")
    minimum = {}

    valid = True
    for draw in draws:
        cubes = re.findall(r"(\d+) (\w+)" , draw )
        for cube in cubes:

            if cube[1] not in minimum: minimum[cube[1]] = 0
            if minimum[cube[1]] < int(cube[0]): minimum[cube[1]] = int(cube[0])

            if cube[1] in capacity.keys():
                if int(cube[0]) > capacity[cube[1]]:
                    valid = False
            else:
                valid = False

    mult_min = 1
    for min_val in minimum.values():
        mult_min = mult_min * min_val
    part2 += mult_min

    if valid:
        part1 +=  int(gameId[0])

print("Part 1:", part1)
print("Part 2:", part2)