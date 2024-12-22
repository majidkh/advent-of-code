from functools import cache

f = open("inputs/22.txt", "r")
numbers = tuple(map(int,f.read().splitlines()))
f.close()

numbers_map = {}

def evolve ( in_number ):

    value = in_number * 64
    in_number = value ^ in_number # Mix
    in_number = int(in_number % 16777216) # Prune

    value = in_number // 32
    in_number = value ^ in_number
    in_number = int(in_number % 16777216) # Prune

    value = in_number * 2048
    in_number = value ^ in_number
    in_number = int(in_number % 16777216) # Prune
    return in_number

sequence_map = {}
unique_sequences = set()

part1 = 0
for number in numbers:
    val = number
    prev_price = val % 10
    numbers_changes = {}
    best_prices = {}

    for i in range(2000):
        val = evolve(val)
        price = val % 10
        change = price - prev_price

        numbers_changes[i] = change
        prev_price = price

        # Calculate the sequence starting on the 4th item ( 0 , 1 , 2 , 3 ...)
        if i > 2:

            sequence = ''
            for j in range( i - 3 , i + 1 ):
                sequence += str(numbers_changes[j]) + ' '
            sequence = sequence.strip()

            numbers_map[str(number) + "_" + str(i)] = [sequence,price]

            if sequence not in best_prices:
                best_prices[sequence] = price
            else:
                if best_prices[sequence] < price:
                    best_prices[sequence] = price

            unique_sequences.add(sequence)

    sequence_map[number] = best_prices

    part1 += val

print("Part 1:", part1)

part2 = 0

for seq in unique_sequences:

    seq_best_offer = 0

    for number in numbers:
        if number in sequence_map:
            if seq in sequence_map[number]:
                seq_best_offer += sequence_map[number][seq]

    if seq_best_offer > part2:
        part2 = seq_best_offer
        print("Best" , part2 , seq )

print("Part 2:", part2 )