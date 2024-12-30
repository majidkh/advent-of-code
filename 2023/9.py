import re

f = open('inputs/9.txt', 'r')
lines = f.read().splitlines()
f.close()

histories = []
for line in lines:
    histories.append(list(map(int, re.findall(r'(-?\d+)', line))))


def pretty_print(history):
    output = ""
    for i in range(len(history)):
        output += " " * (i * 3)
        for j in range(len(history[i])):
            output += f"{history[i][j]: <5}"
        output += "\n"
    print(output)


def predict(numbers):
    rows = [numbers]
    index = 0
    while True:
        current = rows[index]

        new_row = []
        for i in range(len(current) - 1):
            new_row.append(current[i + 1] - current[i])

        rows.append(new_row)
        index += 1

        if len(set(new_row)) == 1 and new_row[0] == 0:
            break

    for i in reversed(range(len(rows))):
        row = rows[i]

        # if its last row
        if len(set(row)) == 1 and row[0] == 0:
            row.append(0)
            row.append(0)
        else:
            row.append(rows[i + 1][-1] + row[-1])
            row.insert(0, row[0] - rows[i + 1][0])

    return rows[0][0], rows[0][-1]


part1 = 0
part2 = 0
for h in histories:
    prediction = predict(h)
    part1 += prediction[1]
    part2 += prediction[0]

print("Part 1:", part1)
print("Part 2:", part2)
