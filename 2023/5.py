import re
from functools import cache

f = open('inputs/5.txt', 'r')
lines = f.read().split("\n\n")
f.close()

seeds = []
maps = []


@cache
def trace(number, map_entry, map_exit):
    for map_ in maps:
        if map_["from"] == map_entry:
            output = number
            for source, destination, range_len in map_["coords"]:
                if destination <= number <= destination + range_len:
                    output = (number - destination) + source
                    break

            if map_["to"] == map_exit:
                return output
            else:
                return trace(output, map_["to"], map_exit)


for category in lines:
    if category.startswith("seeds:"):
        result = re.findall(r"(\d+)", category)
        for r in result:
            seeds.append(int(r))

    else:
        map_name = re.findall("([a-z\-]+) map:", category)
        coords = re.findall("(\d+)", category)
        path = map_name[0].split("-")

        c = []
        for i in range(len(coords) // 3):
            c.append((int(coords[i * 3]), int(coords[i * 3 + 1]), int(coords[i * 3 + 2])))

        maps.append({"from": path[0], "to": path[2], "coords": c})

min_location = float("inf")
for seed in seeds:
    location = trace(seed, "seed", "location")
    if location < min_location:
        min_location = location
print("Part 1 :", min_location)
