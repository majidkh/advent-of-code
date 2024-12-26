f = open("inputs/4.txt", "r")
lines = f.read().splitlines()
f.close()

width = len(lines[0])
height = len(lines)

# find a character in the input data by coordination
def find ( x , y ):

    if width > x >= 0 and height > y >= 0:
        return lines[y][x]
    return ""

# Search for XMAS in different directions
def search ( x , y , offset_x , offset_y ):

    if find ( x , y ) == "X":
        if find ( x + offset_x , y + offset_y ) == "M":
            if find(x +  (offset_x * 2 ), y + (offset_y*2) ) == "A":
                if find(x + (offset_x * 3), y + (offset_y * 3)) == "S":
                    return True

    return False

# Find MAS OR SAM in X Shape
def search_mas( x , y ) :

    if find ( x , y ) == "M" and find ( x + 1 , y + 1 ) == "A" and find ( x + 2 , y + 2 ) == "S":
        if find ( x + 2 , y ) == "S" and find ( x , y + 2 ) == "M":
            return True

        if find ( x + 2 , y ) == "M" and find ( x , y + 2 ) == "S":
            return True

    if find ( x , y ) == "S" and find ( x + 1 , y + 1 ) == "A" and find ( x + 2 , y + 2 ) == "M":
        if find ( x + 2 , y ) == "S" and find ( x , y + 2 ) == "M":
            return True

        if find ( x + 2 , y ) == "M" and find ( x , y + 2 ) == "S":
            return True

    return False

count1 = 0
count2 = 0
for j in range(height):
    for i in range(width):

        # Find XMAS
        for off_x in [-1 , 0 , 1 ]:
            for off_y in [-1 , 0 , 1 ]:
                if search(i, j, off_x, off_y):
                    count1 += 1

        # Find X-MAS
        if search_mas( i , j ):
            count2 += 1

print(count1)
print(count2)