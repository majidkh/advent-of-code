from collections import deque
from functools import reduce
from math import lcm

f = open("inputs/20.txt", "r")
lines = f.read().splitlines()
f.close()

broadcaster = []
modules = {}
connected_inputs = {}

for line in lines:
    if line.startswith("broadcaster"):
        result = line.find("->")
        res = line[result + 2:].strip().split(",")
        for r in res:
            broadcaster.append(r.strip())
    else:
        result = line[1:].split("->")
        m_name = result[0].strip()
        connections = [s.strip() for s in result[1].split(",")]
        m = {"signal": "low", "type": line[0], "connections": connections}
        modules[m_name] = m

        for c in connections:
            if c not in connected_inputs:
                connected_inputs[c] = {}
            connected_inputs[c][m_name] = "low"


def find_feeds(nodes, depth=1):
    feeds = []
    for n in nodes:
        for m_ in modules:
            module_ = modules[m_]
            if n in module_["connections"]:
                feeds.append(m_)

    if depth > 1:
        return find_feeds(feeds, depth - 1)

    return feeds


def flik(sender, conns, signal, counter):
    low_pulses = 1
    high_pulses = 0

    queue = deque()
    for conn in conns:
        queue.append([sender, signal, conn])

    while queue:
        sender, signal, conn = queue.popleft()

        if sender in loops and loops[sender] == 0:
            if signal == "high":
                loops[sender] = counter

        if signal == "low":
            low_pulses += 1
        else:
            high_pulses += 1

        if not conn in modules:
            modules[conn] = {"signal": signal, "type": "test", "connections": []}
        module = modules[conn]

        # Flip-flop module
        if module["type"] == "%":
            if signal == "low":
                if module["signal"] == "low":
                    module["signal"] = "high"
                else:
                    module["signal"] = "low"

                for c_ in module["connections"]:
                    queue.append([conn, module["signal"], c_])


        # Conjunction module
        elif module["type"] == "&":
            connected_inputs[conn][sender] = signal

            mem_signals = set(connected_inputs[conn].values())
            if len(mem_signals) == 1 and next(iter(mem_signals)) == "high":
                for c_ in module["connections"]:
                    queue.append([conn, "low", c_])
            else:

                for c_ in module["connections"]:
                    queue.append([conn, "high", c_])

    return low_pulses, high_pulses


low, high = 0, 0
loops = {}
for r in find_feeds(["rx"], 2):  # Change the depth if needed
    loops[r] = 0

for i in range(10000):
    l, h = flik("broadcaster", broadcaster, "low", i + 1)
    if i < 1000:
        low += l
        high += h

print("Part 1:", low * high)
print("Part 2:", reduce(lcm, list(loops.values()) ))
