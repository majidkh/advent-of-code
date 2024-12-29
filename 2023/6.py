import re

times = []
distances = []

f = open("inputs/6.txt", "r")
for line in f.read().splitlines():
    if line.startswith("Time"):
        times = list(re.findall(r"\d+", line))
    elif line.startswith("Distance"):
        distances = list(re.findall(r"\d+", line))
f.close()

def calculate_ways(time, record):
    ways = 0
    for t in range(time + 1):
        speed = t
        distance = speed * (time - t)
        if distance > record:
            ways += 1
    return ways


part1 = 1
for i in range(len(times)):
    part1 *= calculate_ways(int(times[i]), int(distances[i]))
print("Part1:", part1)

part2 = calculate_ways(int(''.join(times)), int(''.join(distances)))
print("Part2:", part2)
