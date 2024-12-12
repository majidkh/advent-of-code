from functools import cache
import copy
f = open("inputs/12.txt", "r")
data = f.read().splitlines()
f.close()
lines = [list(list(line)) for line in data]

crop_map = copy.deepcopy(lines)
height = len(lines)
width = len(lines[0])

# Get a plant at the given coordination
@cache
def get_plant_at ( col_ , row_ ):
    if 0 <= col_ < width and 0 <= row_ < height:
        return lines[row_][col_]

    return None

# Returns coordinate of the fence, last item is the direction of the fence
def get_fences ( col_, row_ ):

    plant_type = get_plant_at ( col_, row_ )

    result = []

    if get_plant_at(col_ + 1, row_) != plant_type:
        result.append([col_, row_, 1])

    if get_plant_at(col_ - 1, row_) != plant_type:
        result.append([col_, row_, 2])

    if get_plant_at(col_, row_ + 1) != plant_type:
        result.append([col_, row_, 3])

    if get_plant_at(col_, row_ - 1) != plant_type:
        result.append([col_, row_, 4])

    return result


# Get remaining plants left on the map
def get_remaining_plant ( col , row ):
    if 0 <= col < width and 0 <= row < height:
        return crop_map[row][col]

    return None

# Remove a single plant from the map
def remove_plant ( col , row  ):
    crop_map[row][col] = ""

# find connected plants and return the plot
def get_plot ( col , row , blocks ):

    plant_type = get_remaining_plant( col, row )

    if plant_type is None or plant_type == "":
        return blocks

    blocks.append( [ col, row])
    remove_plant(col, row)

    if get_remaining_plant( col + 1 , row ) == plant_type:
        get_plot( col + 1, row , blocks  )

    if get_remaining_plant( col, row + 1 ) == plant_type:
        get_plot ( col , row + 1 , blocks  )

    if get_remaining_plant( col - 1, row  ) == plant_type:
        get_plot ( col - 1 , row , blocks  )

    if get_remaining_plant( col , row - 1  ) == plant_type:
        get_plot ( col  , row - 1 , blocks  )

    return blocks


# part 1
plots = []
total = 0
for j in range( height ):
    for i in range( width ):
        plant_name = get_remaining_plant( i, j)
        if plant_name != "":
            plot = get_plot ( i , j , [] )
            plots.append( plot )
            for plant in plot:
                total += len(get_fences ( plant[0] , plant[1] )) * len(plot)

print(total)

# part 2
total2 = 0
for plot in plots:

    fences = []

    for plant in plot:
        fences.extend ( get_fences( plant[0], plant[1] ) )

    # Now remove fences aligned in the same direction to find edges
    edges =  []

    for i in range(len( fences)):

        found = False

        first_fence = fences[i]

        for second_fence in fences:

            # Check if first fence and second fence are the same direction
            if second_fence[2] == first_fence[2]:

                # Check horizontal fences
                if second_fence[2] == 1 or second_fence[2] == 2:
                    if second_fence[0] == first_fence[0] and second_fence[1] + 1 == first_fence[1]:
                        found = True
                        break

                # Check vertical fences
                if second_fence[2] == 3 or second_fence[2] == 4:
                    if second_fence[0] + 1 == first_fence[0] and second_fence[1] == first_fence[1]:
                        found = True
                        break

        # if first fence doesn't exists, its an edge
        if not found:
            edges.append( first_fence )

    # Calculate the total cost
    total2 += len(edges) * len(plot)

print(total2)
