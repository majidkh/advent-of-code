import copy
f = open("inputs/10.txt", "r")
data = f.read().splitlines()
f.close()
lines = [list(map(int,list(line))) for line in data]
grid_map = copy.deepcopy( lines )

width = len(lines[0])
height = len(lines)

def get_item ( col , row ):
    if col < 0 or col >= width or row < 0 or row >= height:
        return None

    return grid_map[row][col]

def find_possibilities ( node, col , row , score , path , score2 ):

    if node == 9:

        score2 += 1

        if not [col, row] in path:
            path.append( [col , row] )
            score += 1

        return score,score2

    # to right
    right_item = get_item ( col + 1 , row )
    left_item = get_item(col - 1, row)
    up_item = get_item(col, row - 1 )
    down_item = get_item(col, row + 1)

    if right_item is not None and right_item == node + 1 :
        score , score2 = find_possibilities ( right_item , col + 1 , row , score , path , score2 )

    # to left
    if left_item is not None and left_item == node + 1:
        score , score2  = find_possibilities(left_item, col - 1, row , score , path , score2 )

    # to up
    if up_item is not None and up_item == node + 1:
        score , score2  = find_possibilities(up_item, col , row - 1 , score , path , score2 )

    # to down
    if down_item is not None and down_item == node + 1:
        score , score2  = find_possibilities(down_item, col, row + 1 , score , path , score2 )

    return score, score2

total1 = 0
total2 = 0
for x in range(width):
    for y in range(height):
        item = get_item ( x , y)
        if item == 0:
            s1 , s2 = find_possibilities ( item, x, y , 0 , []  , 0)
            total1 += s1
            total2 += s2
print(total1)
print(total2)