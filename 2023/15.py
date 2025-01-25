import re

f = open("inputs/15.txt", "r")
hashes = f.read().split(",")
f.close()


def get_hash(str_value):
    val = 0
    for c in str_value:
        val += ord(c)
        val = (val * 17) % 256

    return val


part1 = 0
for h in hashes:
    part1 += get_hash(h)

print("Part 1:", part1)

boxes = {}

for h in hashes:
    res = re.findall("(\w+)([=-])(\d?)", h)
    label = res[0][0]
    operator = res[0][1]
    focal = res[0][2]
    box = get_hash(label)

    if box not in boxes:
        boxes[box] = {}

    if operator == "-":
        if label in boxes[box]:
            del boxes[box][label]

    if operator == "=":
        boxes[box][label] = focal

part2 = 0
for box in boxes:
    for index, lense in enumerate(boxes[box].keys()):
        part2 += (box + 1) * (index + 1) * int(boxes[box][lense])

print("Part 2:", part2)
