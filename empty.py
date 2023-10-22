# empty.py kan användas som träningskod som raderas varje övningspass, 
# testa din förståelse och radera efteråt.

grid = [[0 for _ in range(9)] for _ in range(9)]

for list in grid:
    print(list)

print('\n')

def valid(grid, row, col, num):
    # Check if the number already exists in the current row or column
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False

    # Check if the number exists in the current 3x3 box
    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True

def solve(grid, row=0, col=0):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve(grid, row, col + 1)

    for num in range(1, 10):
        if valid(grid, row, col, num):
            grid[row][col] = num
            if solve(grid, row, col + 1):
                return True

    grid[row][col] = 0
    return False

solve(grid)

for list in grid:
    print(list)