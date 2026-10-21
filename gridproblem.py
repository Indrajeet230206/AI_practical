grid = [
    ['S','.','.'],
    ['X','X','.'],
    ['.','.','G']
]

row = 0
col = 0
visited = []

while True:
    print("current positioin:",(row,col))
    visited.append((row,col))

    if(grid[row][col]=='G'):
        print("goal reached")
        break

    if col < 2 and grid[row][col+1] != 'X':
        col = col + 1

    elif row < 2 and grid[row + 1][col] != 'X':
        row = row + 1

    else:
        print("path not found")
        break

print("visited positions: ",visited)
