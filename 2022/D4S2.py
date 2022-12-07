def intersect(a, b):
    i = [v for v in a if v in b]
    return i


count = 0
with open('D4_input.txt', 'r') as f:
    for l in f:
        l = [list(map(int, s.split('-'))) for s in l.split('\n')[0].split(',')]
        a = list(range(l[0][0], l[0][1] + 1))
        b = list(range(l[1][0], l[1][1] + 1))
        i = intersect(a, b)
        if len(i) > 0:
            count += 1

print(count)
