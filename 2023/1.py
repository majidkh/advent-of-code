import re
f = open('inputs/1.txt')
lines = f.read().splitlines()
f.close()

def calculate():
    sums = 0
    for line in lines:
        numbers = re.findall(r'(\d)', line)
        if len(numbers) >= 1:
            sums += int(numbers[0] + numbers[-1])
    return sums

print("part 1:", calculate())

