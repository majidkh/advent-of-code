f = open("inputs/5.txt", "r")
lines = f.read().splitlines()
f.close()

rules = []
page_numbers = []

# Data extraction
for line in lines:

    # Extract rules
    if line.find("|") >= 0:
        rules.append( list(map(int, line.split("|"))) )

    # Extract pages
    if line.find(",") >= 0:
        page_numbers.append( list(map(int, line.split(","))) )

#print(rules)
#print(page_numbers)
# Logic

def is_valid ( numbers ):

    valid = True

    for i in range(len(numbers)):
        number = numbers[i]

        for r in rules:

            # validate this number before the value
            if r[0] == number:
                if r[1] in numbers and numbers.index ( r[1]) <= i:
                    valid = False

            # check if this number comes after value
            if r[1] == number:
                if r[0] in numbers and numbers.index (r[0]) >= i:
                    valid = False

    return valid


def make_correct ( numbers):

    result = []
    for i in range(len(numbers)):
        number = numbers[i]

        for r in rules:

            # validate this number before the value
            if r[0] == number:

                if r[1] in numbers and  numbers.index(r[1]) <= i:

                    # swap indexes
                    numbers[i], numbers[ numbers.index(r[1]) ] = numbers[ numbers.index(r[1]) ], numbers[i]


            # check if this number comes after value
            if r[1] == number:
                if r[0] in numbers and numbers.index(r[0]) >= i:
                    # swap indexes
                    numbers[i], numbers[numbers.index(r[0])] = numbers[numbers.index(r[0])], numbers[i]

    return numbers

result1 = 0
result2 = 0
for n in page_numbers:
    if is_valid(n):
        result1 += n[  int ( (len(n) -1 ) / 2 ) ]
    else:

        while not is_valid(n):
            n = make_correct(n)

        result2 += n[  int ( (len(n) -1 ) / 2 ) ]



print(result1)
print(result2)



