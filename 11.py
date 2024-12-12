from functools import cache

f = open("inputs/11.txt", "r")
input_file = f.read()
f.close()

items = list(map(int,input_file.split(" ")))

counter = 0

@cache
def get_length( value , blink):

    if blink == 0: return 1

    str_value = str(value)

    if value == 0 :
        return get_length( 1, blink - 1)

    elif len(str_value) % 2 == 0:

        middle = int(len(str_value) / 2)
        part1 = int(str_value[:middle])
        part2 = int(str_value[middle:])

        return get_length(part1, blink - 1) + get_length(part2, blink - 1)

    else:
        return get_length( value * 2024 , blink -1 )

length = 0
for s in range(len(items)):

    length +=  get_length ( items[s] , 75 )

print(length)