with open('D6_input.txt', 'r') as f:
    l = list(f.readline())
    for i in range(3, len(l)):
        sub = l[i - 3:i + 1]
        if len(set(sub)) == 4:
            print(i + 1)
            break
