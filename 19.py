from functools import cache

f = open("inputs/19.txt", "r")
lines = f.read().split("\n\n")
f.close()
patterns = lines[0].strip().split(",")
patterns = [pattern.strip() for pattern in patterns]

designs = lines[1].strip().split("\n")


seens = []
def is_possible ( design_ , options_ , unique ):

    if len(design_) == 0:
        options_ += 1
        return options_


    for p in patterns:
        if design_.startswith(p):
            options_ = is_possible ( design_[len(p):] , options_ , unique )

            if unique and options_ > 0 :
                return 1

    return options_

part1 = 0
for design in designs:
    options = is_possible( design , 0 , True )

    part1 += options

print("Part 1:", part1)
