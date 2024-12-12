import re
f = open("inputs/1.txt", "r")
lines = f.read().splitlines()
f.close()

list1 = []
list2 = []
for line in lines:
    digits = re.findall(r"\d+", line)
    if len(digits) == 2:
        list1.append(int(digits[0]))
        list2.append(int(digits[1]))

list1.sort()
list2.sort()

distance = 0
occurrences = 0
for i in range(len(list1)):
    distance += abs(list1[i] - list2[i])
    occurrences += list2.count(list1[i]) * list1[i]

print(distance)
print(occurrences)
