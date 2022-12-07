with open('D6_input.txt', 'r') as f:
    l = list(f.readline())
    for i in range(13, len(l)):
        sub = l[i - 13:i + 1]
        if len(set(sub)) == 14:
            print(i + 1)
            break
