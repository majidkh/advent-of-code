import re
from functools import cmp_to_key

f = open("inputs/7.txt", "r")
lines = f.read().splitlines()
f.close()

hands = []
for line in lines:
    hands.append((line[:5], int(list(re.findall("(\d+)", line[6:]))[0])))


def get_hand_type(hand, use_joker=False):
    cards = {}
    for card in hand[0]:
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1

    if use_joker:
        jokers = hand[0].count("J")
        if jokers > 0:
            print(hand) # TODO

    cards = sorted(cards.values(), reverse=True)

    # High card
    if len(cards) == 5:
        return 1

    # 1 Pair
    elif len(cards) == 4:
        return 2

    elif len(cards) == 3:

        # 2 pairs
        if cards[0] == 2 and cards[1] == 2:
            return 3

        # 3 of a kind
        elif cards[0] == 3:
            return 4

    elif len(cards) == 2:

        # Full house
        if cards[0] == 3:
            return 5

        # 4 of a kind
        elif cards[0] == 4:
            return 6

    # 5 of a kind
    elif len(cards) == 1:
        return 7

    return 0


labels1 = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}
labels2 = {"A": 13, "K": 12, "Q": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "J": 1}


def compare_cards(hand1, hand2, labels):
    for i in range(len(hand1)):
        if hand1[i] != hand2[i]:
            if labels[hand1[i]] < labels[hand2[i]]:
                return -1
            else:
                return 1
    return 0


def compare_part_1(hand1, hand2):
    if hand1[1] > hand2[1]:
        return 1
    elif hand1[1] < hand2[1]:
        return -1
    return compare_cards(hand1[0][0], hand2[0][0], labels1)


deck = []

for h in hands:
    deck.append((h, get_hand_type(h)))
deck.sort(key=cmp_to_key(compare_part_1))

part1 = 0
for i in range(len(deck)):
    h = deck[i]
    part1 += (i + 1) * h[0][1]
print("Part 1:", part1)
