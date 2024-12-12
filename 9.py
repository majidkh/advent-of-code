import re,copy
f = open("inputs/9.txt", "r")
input_file = f.read()
f.close()

data = list(map(int, input_file))

# create the block first
index = 0
file_id = 0

block  = []
block2 = []
while True:

    # Files
    files = []
    for i in range( data[index] ):
        files.append( file_id )
        block.append( file_id )

    block2.append( files)

    index += 1
    file_id += 1

    if index >= len(data):
        break

    # Free space
    free_space = []
    for i in range( data[index] ):
        block.append( '.' )
        free_space.append( '.')
    block2.append( free_space )

    index += 1

    if index >= len(data):
        break

# De-Fragment!
block = list(block)
block2 = copy.deepcopy(block)

def find_last_digit ():

    for j in range( len(block) ):

        if isinstance(block[ (len(block)- 1 ) - j ], int):

            end_index = (len(block) - 1 ) - j

            return end_index

for i in range( len(block) ):

    if block[i] == '.':

        last_char_idx = find_last_digit()

        if last_char_idx > i :
            block[i] = block[last_char_idx]
            block[last_char_idx] = '.'
        else:
            break

# Calculate checksum
checksum = 0
for i in range( len(block) ):

    if isinstance(block[i], int):
        checksum += int(block[i]) * i


print(checksum)

pointer = len(block2) - 1
start_index = -1

while pointer >= 0:

    current_digit = block2[pointer]

    if isinstance( current_digit , int ):

        file_length = 1
        while block2[pointer-1] == current_digit:
            file_length += 1
            pointer -= 1

        # Now find space at the left
        space_index = 0
        while space_index < pointer:

            if block2[space_index] == '.':
                space_length = 1
                while block2[ space_index + 1 ] == '.':
                    space_length += 1
                    space_index += 1

                if space_length >= file_length:

                    space_start = space_index + 1 - space_length

                    # move them
                    for i in range( file_length ):
                        block2[ space_start + i ] = current_digit
                        block2[pointer + i ] = '.'

                    break

            space_index += 1

    pointer -= 1


# Calculate checksum
checksum = 0
for i in range( len(block2) ):

    if isinstance(block2[i], int):
        checksum += int(block2[i]) * i


print(checksum)