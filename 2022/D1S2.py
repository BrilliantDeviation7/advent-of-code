with open('D1_input.txt', 'r') as f:
    calories = []
    currentCalorie = 0
    for line in f:
        if line == '\n':
            calories.append(currentCalorie)
            currentCalorie = 0
        else:
            currentCalorie += int(line)
    calories.sort()
    # print(calories)
    print(sum(calories[-3:]))
