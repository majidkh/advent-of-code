import re
from collections import deque
from functools import cache

f = open("inputs/21.txt", "r")
codes = f.read().splitlines()
f.close()

numpad = ('7','8','9'),('4','5','6'),('1','2','3'),('','0','A')
keypad = ('','^','A'),('<','v','>')

numpad_map = {}
for row in range(len(numpad)):
    for col in range(len(numpad[row])):
        numpad_map[numpad[row][col]] = (col, row)
        numpad_map[(col,row)] = numpad[row][col]

keypad_map = {}
for row in range(len(keypad)):
    for col in range(len(keypad[row])):
        keypad_map[keypad[row][col]] = (col, row)
        keypad_map[(col,row)] = keypad[row][col]

robots = [numpad_map['A']]
for i in range(3):
    robots.append(keypad_map['A'])

@cache
def find_path( code , depth , use_numpad = True):

    if depth == -1: return len(code)
    keyboard = keypad_map
    if use_numpad:
        keyboard = numpad_map
    start = keyboard['A']

    length = 0

    for c in code:
        target = keyboard[c]
        path = deque([( start[0], start[1] , "")])
        shortest = float('inf')

        while path:
            x,y,sequence = path.popleft()
            if keyboard[(x,y)] == "": continue

            if (x,y) == target:

                l = find_path( sequence + "A" , depth -1 , False )
                if l < shortest:
                    shortest = l

            if target[0] > x :
                path.append( (x + 1 , y , sequence + ">") )

            if target[0] < x :
                path.append( (x - 1 , y , sequence + "<") )

            if target[1] > y :
                path.append( (x  , y + 1 , sequence + "v") )

            if target[1] < y :
                 path.append( (x  , y - 1 , sequence + "^") )

        length += shortest
        start = target
    return length


part1 = 0
for c in codes:
    val = re.findall("(\d+)" , c )
    part1 += find_path( c , 2  ) * int(val[0])
print(part1)

part2 = 0
for c in codes:
    val = re.findall("(\d+)" , c )
    part2 += find_path( c , 25  ) * int(val[0])

print(part2)