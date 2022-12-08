with open('D8_input.txt', 'r') as f:
    grid = [list(map(int, list(l[:-1]))) for l in f.readlines()]
    # cannot use result = grid.copy()
    # because nested lists are still same objects
    result = [arr[:] for arr in grid]
    for i_r, r in enumerate(grid):
        for i_c in range(len(r)):
            column = [row[i_c] for row in grid]
            if i_r in [0, len(r) - 1] or i_c in [0, len(r) - 1]:
                result[i_r][i_c] = 1
            elif r[i_c] > max(r[:i_c]) or r[i_c] > max(r[i_c + 1:]):
                result[i_r][i_c] = 1
            elif r[i_c] > max(column[:i_r]) or r[i_c] > max(column[i_r + 1:]):
                result[i_r][i_c] = 1
            else:
                result[i_r][i_c] = 0
    print(sum(sum(r1) for r1 in result))
