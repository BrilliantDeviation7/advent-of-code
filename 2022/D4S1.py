count = 0
with open('D4_input.txt', 'r') as f:
    for l in f:
        l = [s.split('-') for s in l.split('\n')[0].split(',')]
        if int(l[0][0]) >= int(l[1][0]) and int(l[0][1]) <= int(l[1][1]):
            count += 1
        elif int(l[0][0]) <= int(l[1][0]) and int(l[0][1]) >= int(l[1][1]):
            count += 1
print(count)
