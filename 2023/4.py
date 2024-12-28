import re

f = open('inputs/4.txt', 'r')
lines = f.read().splitlines()
f.close()

part1 = 0
part2 = 0
copies = {}

for line in lines:
    cards = line.split("|")
    winning_card = re.findall(r"(\d+)", cards[0])
    my_numbers = re.findall(r"(\d+)", cards[1])
    wins = set(winning_card[1:]).intersection(my_numbers)
    card_number = int(winning_card[0])

    index = 0
    if card_number in copies:
        index = copies[card_number]

    for j in range(index + 1):
        part2 += 1
        for i in range(1, len(wins) + 1):
            if card_number + i not in copies:
                copies[card_number + i] = 1
            else:
                copies[card_number + i] += 1
        if j == 0 and len(wins) > 0:
            part1 += 2 ** (len(wins) - 1)

print("Part 1:", part1)
print("Part 2:", part2)
