with open('input.txt', 'r') as file:
    input = file.read()

grid = [list(row) for row in input.strip().split("\n")]
rows, cols = len(grid), len(grid[0])

# up, right, down, left
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# starting position and direction
for r in range(rows):
    for c in range(cols):
        if grid[r][c] in "^>v<":
            guard_pos = (r, c)
            direction_index = "^>v<".index(grid[r][c])
            grid[r][c] = "."
            break

visited = set()
visited.add(guard_pos)

step = 0
max_steps = rows * cols * 4 

while step < max_steps:
    dr, dc = directions[direction_index]
    next_pos = (guard_pos[0] + dr, guard_pos[1] + dc)

    if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
        break  # exit when guard moves out of bounds

    # check if forward movement is possible
    if grid[next_pos[0]][next_pos[1]] != "#":
        guard_pos = next_pos
        visited.add(guard_pos)
    else:
        direction_index = (direction_index + 1) % 4 # turn right

    step += 1

if step >= max_steps:
    print("Maximum step limit reached.")

print(f"Positions visited: {len(visited)}")

# final map with visited positions
# for r in range(rows):
#     for c in range(cols):
#         if (r, c) in visited:
#             print("X", end="")
#         else:
#             print(grid[r][c], end="")
#     print()