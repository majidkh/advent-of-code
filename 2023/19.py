import re
from functools import reduce
from operator import mul

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

part2 = 0


def is_range_valid(range_):
    if range_[0] > range_[1]:
        return False

    return True


def check_accepted(node, xmas):
    result = 0

    workflow = workflows[node]
    for w in workflow:

        for pp in xmas:

            dest = w["d"]
            part_range = xmas[pp]
            if not is_range_valid(part_range): continue

            yes = part_range
            no = None

            if "v" in w:

                if w["v"] != pp: continue

                opr = w["o"]
                target = w["n"]

                if opr in "<>":
                    yes = (part_range[0], target - 1)
                    no = (target, part_range[1])
                    if opr == ">":
                        yes = (target + 1, part_range[1])
                        no = (part_range[0], target)

            if is_range_valid(yes):

                xmas2 = xmas.copy()
                xmas2[pp] = yes

                if dest == "A":

                    numbers = []
                    for t in xmas2:
                        numbers.append(xmas2[t][1] - xmas2[t][0] + 1)

                    result += reduce(mul, numbers)


                elif dest == "R":
                    result += 0
                else:

                    result += check_accepted(dest, xmas2)

            if no is not None:
                xmas[pp] = no
                continue

            if "v" not in w:
                return result

    return result


xmas_all = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}

print("Part 2:", check_accepted("in", xmas_all))
