with open('D2_input.txt', 'r') as f:
    win = ["A Y", "B Z", "C X"]
    tie = ["A X", "B Y", "C Z"]
    score = 0
    for line in f:
        score += "XYZ".find(line[2]) + 1
        if line[:3] in tie:
            score += 3
        elif line[:3] in win:
            score += 6
        # print(score)
    print(score)
