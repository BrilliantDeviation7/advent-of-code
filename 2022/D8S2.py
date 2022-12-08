def calcScore(r, c, g):
    up = 0
    down = 0
    left = 0
    right = 0

    treeHeight = grid[r][c]

    # up (rows above: r - 1 -> 0)
    for i in range(r - 1, -1, -1):
        up += 1
        if grid[i][c] >= treeHeight:
            break

    for i in range(r + 1, len(g)):
        down += 1
        if grid[i][c] >= treeHeight:
            break

    for i in range(c - 1, -1, -1):
        left += 1
        if grid[r][i] >= treeHeight:
            break

    for i in range(c + 1, len(g[r])):
        right += 1
        if grid[r][i] >= treeHeight:
            break

    return up * down * right * left


with open('D8_input.txt', 'r') as f:
    grid = [list(map(int, list(l[:-1]))) for l in f.readlines()]
    maxScore = 0
    for i_r, r in enumerate(grid):
        for i_c, v in enumerate(r):
            score = calcScore(i_r, i_c, grid)
            if score > maxScore:
                maxScore = score
    print(maxScore)
