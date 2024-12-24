with open('input.txt', 'r') as file:
    input = file.read()


grid = [list(line.strip()) for line in input.strip().splitlines()]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
count = 0
word = "XMAS"
word_length = len(word)
rows = len(grid)
cols = len(grid[0])

# part 1
def check_direction(grid, word, start_row, start_col, row_step, col_step):
    for i in range(len(word)):
        r = start_row + i * row_step
        c = start_col + i * col_step
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != word[i]:
            return False
    return True

for row in range(rows):
    for col in range(cols):
        for row_step, col_step in directions:
            if check_direction(grid, word, row, col, row_step, col_step):
                count += 1

print(f"The word 'XMAS' appears {count} times.")

# part 2
def check_xmas_direction(x, y, grid):
    word1 = grid[x+1][y-1]+grid[x][y]+grid[x-1][y+1]
    word2 = grid[x-1][y-1]+grid[x][y]+grid[x+1][y+1]
    if word1 in ['MAS','SAM'] and word2 in ['MAS','SAM']:
        return True
    return False

count = 0
for row in range(1, rows-1):
    for col in range(1, cols-1):
        if check_xmas_direction(row, col, grid):
            count += 1

print(f"The word X-'MAS' appears {count} times.")
