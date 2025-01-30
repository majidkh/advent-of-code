import heapq

f = open('inputs/17.txt', 'r')
data = f.read().splitlines()
f.close()
grid = [list(map(int, line)) for line in data]

width = len(grid[0])
height = len(grid)
end = (width - 1, height - 1)

reverse_directions = {"<>", "><", "^v", "v^"}


def find_path():
    x, y = (0,0)
    nodes = []  # Heat loss , x , y , direction , direction count
    heapq.heappush(nodes, (0, x, y, "", 0))  # Start with (distance 0, city 'A')

    seen = {}

    while nodes:

        loss, x, y, direction, count = heapq.heappop(nodes)

        if (x, y) == end:
            if loss <= float("inf"):
                return loss

        neighbours = [(1, 0, ">"), (-1, 0, "<"), (0, 1, "v"), (0, -1, "^")]

        for i, j, d in neighbours:

            nx, ny = (x + i, y + j)
            if nx < 0 or nx >= width or ny < 0 or ny >= height: continue

            if d + direction in reverse_directions: continue
            if count >= 3 and d == direction: continue

            nc = 1
            if d == direction: nc = count + 1

            new_loss = grid[ny][nx] + loss
            if (nx, ny, d, nc) not in seen or seen[nx, ny, d, nc] > new_loss:
                heapq.heappush(nodes, (new_loss, nx, ny, d, nc))
                seen[nx, ny, d, nc] = new_loss

    return None


print("Part 1:", find_path())
