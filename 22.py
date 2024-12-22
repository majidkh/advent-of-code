f = open("inputs/22.txt", "r")
numbers = list(map(int,f.read().splitlines()))
f.close()

def evolve ( in_number ):

    val = in_number * 64
    in_number = val ^ in_number # Mix
    in_number = int(in_number % 16777216) # Prune

    val = in_number // 32
    in_number = val ^ in_number
    in_number = int(in_number % 16777216) # Prune

    val = in_number * 2048
    in_number = val ^ in_number
    in_number = int(in_number % 16777216) # Prune


    return in_number


part1 = 0
for number in numbers:
    for i in range(2000):
        number = evolve(number)
    part1 += number

print("Part 1:", part1)

