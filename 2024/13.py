import re
f = open("inputs/13.txt", "r")
machines = f.read().split("\n\n")
f.close()

def calculate_tokens ( a , b , p):
    total = 0

    claw = [0, 0]
    claw[0] = (p[0] * b[1] - p[1] * b[0]) / (a[0] * b[1] - a[1] * b[0])
    claw[1] = (p[0] - a[0] * claw[0]) / b[0]

    if claw[0] % 1 == claw[1] % 1 == 0:
        total += int((claw[0] * 3) + claw[1])

    return total

part1 = 0
part2 = 0
for machine in machines:

    data = list(map(int,re.findall(r"(\d+)", machine)))
    button_a = [data[0],data[1]]
    button_b = [data[2],data[3]]
    prize = [data[4],data[5]]

    part1 += calculate_tokens(button_a, button_b, prize)

    prize[0] += 10000000000000
    prize[1] += 10000000000000
    part2 += calculate_tokens(button_a, button_b, prize)

print( part1 )
print( part2 )
