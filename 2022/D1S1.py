with open('D1_input.txt', 'r') as f:
    maxCalorie = 0
    currentCalorie = 0
    for line in f:
        if line == '\n':
            if currentCalorie > maxCalorie:
                maxCalorie = currentCalorie
            currentCalorie = 0
        else:
            currentCalorie += int(line)
print(maxCalorie)
