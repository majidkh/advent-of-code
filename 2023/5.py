import copy
import re

f = open('inputs/5.txt', 'r')
lines = f.read().split("\n\n")
f.close()

seeds = []
maps = []

# Data Extraction
for category in lines:
    if category.startswith("seeds:"):
        results = re.findall(r"(\d+)", category)
        for result in results:
            seeds.append(int(result))

    else:
        map_name = re.findall("([a-z\-]+) map:", category)
        coords = re.findall("(\d+)", category)
        path = map_name[0].split("-")

        c = []
        for i in range(len(coords) // 3):
            c.append((int(coords[i * 3]), int(coords[i * 3 + 1]), int(coords[i * 3 + 2])))

        maps.append({"from": path[0], "to": path[2], "coords": c})


def calculate(inputs, map_entry, map_exit):
    output = []

    for map_ in maps:
        if map_["from"] == map_entry:

            for number in inputs:
                min_val = float("inf")
                max_val = 0
                for s, d, r in map_["coords"]:
                    e = d + r  # end position
                    if d < min_val: min_val = d
                    if e > max_val: max_val = e

                # Out of range numbers s---e [----] s---e
                if number[0] > max_val or number[1] < min_val:
                    output.append(number)
                    continue

                # 4. out intersection s--[------]--e
                if number[0] < min_val and number[1] > max_val:
                    inputs.append((number[0], min_val - 1))
                    inputs.append((min_val, max_val))
                    inputs.append((max_val + 1, number[1]))
                    continue

                # Loop through map coords
                for s, d, r in map_["coords"]:
                    e = d + r  # end position
                    o = s - d  # offset

                    # 1. Number range is inside the range [---s---e--]
                    if number[0] >= d and number[1] <= e:
                        output.append((number[0] + o, number[1] + o))

                    # 2. intersection right [--s---]--e
                    elif d <= number[0] <= e < number[1]:
                        output.append((number[0] + o, e + o))
                        inputs.append((e + 1, number[1]))

                    # 3. intersection left s--[--e---]
                    elif number[0] < d <= number[1] <= e:
                        output.append((d + o, number[1] + o))
                        inputs.append((number[0], d - 1))

            if map_["to"] == map_exit:
                return output
            else:
                return calculate(output, map_["to"], map_exit)

    return output


numbers = []
for i in seeds:
    numbers.append((i,i))

print("Part 1:", min(calculate(numbers, "seed", "location"))[0])

numbers = []
for i in range(len(seeds) // 2):
    from_num = seeds[i * 2]
    to_num = seeds[(i * 2) + 1]
    numbers.append((from_num, from_num + to_num - 1))

print("Part 2:", min(calculate(numbers, "seed", "location"))[0])
