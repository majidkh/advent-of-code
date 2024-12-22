from collections import deque
from functools import cache

f = open("inputs/22.txt", "r")
numbers = tuple(map(int,f.read().splitlines()))
f.close()

@cache
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

@cache
def get_offer ( secrets, sequence ):
    result = []

    for secret in secrets:
        pointer = 0
        prev_price = secret % 10

        offers = []

        for _ in range(2000):
            secret = evolve(secret)
            price = secret % 10
            change = price - prev_price

            # Find the sequence
            if change == sequence[pointer]:
                pointer += 1
                if pointer >= len(sequence):
                    offers.append( price )
                    pointer = 0
            else:
                pointer = 0

            prev_price = price

        if len(offers)> 0:
            result.append( max(offers ))


    return sum(result)

# Find all 4 sequences
def find_sequences( secrets ):

    result = []

    seq = deque()

    for secret in secrets:
        prev_price = secret % 10
        for _ in range(2000):
            secret = evolve(secret)
            price = secret % 10
            change = price - prev_price

            seq.append(change)

            if len(seq) > 4:
                seq.popleft()

            if len(seq) == 4 and list(seq) not in result:
                result.append(tuple(seq))

            prev_price = price

    return result

sequences = find_sequences(numbers)

part2 = 0
for i in range( len(sequences) - 1 ):
    percent = int((i * 100 ) / (len(sequences) - 1 ))
    if percent % 2 ==  0:
        print(f"{percent} %")

    offer = get_offer( numbers, tuple(sequences[i]))
    if offer > part2:
        part2 = offer

print("Part 2:", part2)
