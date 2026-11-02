N = 8
cols = []                                  # cols[c] = row of queen in column c

def safe(row, col):
    return all(r != row and abs(r - row) != col - c for c, r in enumerate(cols))

def solve(col):
    if col == N: return True
    for row in range(N):
        if safe(row, col):
            cols.append(row)               # PLACE
            if solve(col + 1): return True
            cols.pop()                     # BACKTRACK
    return False

if solve(0):
    for r in cols: print(". " * r + "Q " + ". " * (N - r - 1))
