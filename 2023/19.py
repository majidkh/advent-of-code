import re

f = open("inputs/19.txt", "r")
lines = f.read().splitlines()
f.close()

workflows = {}
parts = []

for line in lines:

    if line.startswith("{"):
        data = list(map(int, re.findall(r"(\d+)", line)))
        parts.append({"x": data[0], "m": data[1], "a": data[2], "s": data[3]})
    else:

        data = re.findall(r"(\w+){(.+)}", line)
        if len(data) > 0:
            w_name = data[0][0]
            flows = []
            for flow in data[0][1].split(","):
                res = re.findall(r"(\w)([<>])(\d+):(\w+)", flow)
                if len(res) > 0:
                    flows.append({"v": res[0][0], "o": res[0][1], "n": int(res[0][2]), "d": res[0][3]})
                else:
                    flows.append({"d": flow})

            workflows[w_name] = flows


def sort_ratings(xmas, node="in"):
    workflow = workflows[node]

    for w in workflow:
        for n in xmas:
            rating = xmas[n]
            valid = False

            if "v" not in w:
                valid = True
            else:
                if w["v"] == n and w["o"] == ">" and rating > w["n"]:
                    valid = True
                elif w["v"] == n and w["o"] == "<" and rating < w["n"]:
                    valid = True

            if valid:
                if w["d"] == "A":
                    return True
                elif w["d"] == "R":
                    return False
                else:
                    return sort_ratings(xmas, w["d"])

    return False


part1 = 0
for p in parts:
    if sort_ratings(p):
        part1 += sum(p.values())

print("Part 1:", part1)
