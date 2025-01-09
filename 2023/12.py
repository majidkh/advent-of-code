import re
import time

f = open('inputs/12.txt', 'r')
lines = f.read().splitlines()
f.close()

data = []
data2 = []

for line in lines:
    parts = line.split(' ')
    values = tuple(map(int, parts[1].split(",")))
    data.append([parts[0], values])

    # For Part 2
    s = (parts[0] + "?") * 5
    v = (parts[1] + ",") * 5
    v = v[:-1]
    values2 = tuple(map(int, v.split(",")))
    data2.append([s, values2])



def is_valid(combination, numbers):
    if combination.count("#") != sum(numbers):
        return False

    springs = re.findall(r"(#+)", combination)
    if len(springs) != len(numbers): return False
    for i in range(len(springs)):
        if len(springs[i]) != numbers[i]: return False
    return True

seen = set()
def get_combinations(signature, numbers, count=0):

    pointer = signature.find("?")
    if pointer == -1:
        if is_valid(signature, numbers):
            return count + 1
        return count

    if signature.count("#") > sum(numbers):
        return count


    # Check if first digit is met
    ci = 0
    ni = 0
    for ch in signature:
        if ni >= len(numbers):
            break
        if ch == "?":
            break
        elif ch == "#":
            ci += 1
        elif ch == ".":
            if ci > 0:
                if numbers[ni] != ci:
                    return count
                else:
                    ni += 1
                    ci = 0

    for i in ".#":
        combination = signature[0:pointer] + i + signature[pointer + 1:]
        c = get_combinations(combination, numbers, count)
        if c is not None:
            count = c

    return count


part1 = 0
for s, v in data:
    part1 += get_combinations(s, v)
print("Part 1:", part1)
