from utils.advent_input_parser import parse_grid

with open('04/input.txt', 'r') as file:
    text = file.read()
grid = parse_grid(text)


def check_for_ms_around_a(i,j,matrix_len):
    res = 0   
    if i-1 >= 0 and j-1 >= 0 and i+1 < matrix_len and j+1 < matrix_len:
        if grid[i-1][j-1] == 'M' and grid[i+1][j+1] == 'S':
            res+=1
        if grid[i-1][j+1] == 'M' and grid[i+1][j-1] == 'S':
            res+=1
        if grid[i+1][j-1] == 'M' and grid[i-1][j+1] == 'S':
            res+=1
        if grid[i+1][j+1] == 'M' and grid[i-1][j-1] == 'S':
            res+=1
    if res > 1:
        return True
    else:
        return False
   
result = 0
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == 'A' and check_for_ms_around_a(i, j, len(grid)):
            result+=1
print(result)