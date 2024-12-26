import itertools
f = open("inputs/7.txt", "r")
lines = f.read().splitlines()
f.close()



def compare_sum ( in_numbers, instructions , in_value ):

    for instruction in instructions:

        total = in_numbers[0]

        for i in range(len(in_numbers) - 1 ):

            if instruction[i] == "+":
                total += in_numbers[i + 1]

            if instruction[i] == "*":
                total *= in_numbers[i + 1 ]

            if instruction[i] == "|":
                total = int(str(total) + str(in_numbers[i + 1]))

        if total == in_value:
            return True

    return False

def is_valid( in_numbers , letters , in_value):

    instructions = [''.join(c) for c in itertools.product(letters, repeat= len(in_numbers) - 1)]
    return compare_sum ( in_numbers, instructions, in_value )


result1 = 0
result2 = 0

for line in lines:

    value = int(line[0:line.find(":")])
    numbers = list(map(int,line[line.find(":") + 2:].split(" ")))

    if is_valid( numbers, "+*", value):
        result1 += value

    if is_valid( numbers, "+*|", value):
        result2 += value

print(result1)
print(result2)