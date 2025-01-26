f = open('inputs/16.txt', 'r')
lines = f.read().splitlines()
f.close()

width = len(lines[0])
height = len(lines)

def pretty_print ( grid):
    output = ""
    for row in grid:
        for col in row:
            output += col
        output += "\n"
    print(output)


def calculate_energizes( start_beam ):

    beams = [start_beam]
    seen = set()
    seen.add(tuple(beams[0]))
    grid = [['.' for _ in range(width)] for _ in range(height)]

    while len(beams) > 0:

        for index, beam in enumerate(beams):
            beam[0] += beam[2]
            beam[1] += beam[3]
            nx, ny = (beam[0], beam[1])

            if nx < 0 or nx >= width or ny < 0 or ny >= height:
                del beams[index]
                break

            key = tuple(beam)
            if key in seen:
                del beams[index]
                continue
            seen.add(key)

            grid[ny][nx] = "#"

            # Split the beam
            if lines[ny][nx] == "|" and beam[2] in [1, -1]:
                beams[index][2] = 0
                beams[index][3] = 1
                beams.append([nx, ny, 0, -1])

            if lines[ny][nx] == "-" and beam[3] in [1, -1]:
                beams[index][2] = 1
                beams[index][3] = 0
                beams.append([nx, ny, -1, 0])

            # reflect
            elif lines[ny][nx] == "/":
                if beam[2] == 1:  # Moving right
                    beams[index][2] = 0
                    beams[index][3] = -1
                elif beam[2] == -1:  # Moving left
                    beams[index][2] = 0
                    beams[index][3] = 1
                elif beam[3] == 1:  # Moving down
                    beams[index][2] = -1
                    beams[index][3] = 0
                elif beam[3] == -1:  # Moving up
                    beams[index][2] = 1
                    beams[index][3] = 0

            elif lines[ny][nx] == "\\":
                if beam[2] == 1:  # Moving right
                    beams[index][2] = 0
                    beams[index][3] = 1
                elif beam[2] == -1:  # Moving left
                    beams[index][2] = 0
                    beams[index][3] = -1
                elif beam[3] == 1:  # Moving down
                    beams[index][2] = 1
                    beams[index][3] = 0
                elif beam[3] == -1:  # Moving up
                    beams[index][2] = -1
                    beams[index][3] = 0

    return sum(cell == '#' for row in grid for cell in row)

part1 = calculate_energizes([-1,0,1,0])
print("Part 1:", part1)

beam_starts = []
for col in range(width):
    beam_starts.append([col, -1, 0, 1])
    beam_starts.append([col, height, 0, -1])

for row in range(height):
    beam_starts.append([-1, row, 1, 0])
    beam_starts.append([ width, row, -1, 0])

part2 = 0
for start in beam_starts:
    res = calculate_energizes(start)
    if res > part2:
        part2 = res

print( "Part 2:", part2 )