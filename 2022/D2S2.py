with open('D2_input.txt', 'r') as f:
    win = ["A 2", "B 3", "C 1"]
    tie = ["A 1", "B 2", "C 3"]
    lose = ["A 3", "B 1", "C 2"]
    score = 0
    for line in f:
        # print(list(line))
        if line[2] == "X":
            for play in lose:
                if play[0] == line[0]:
                    score += int(play[2]) + 0
                    break
        elif line[2] == "Y":
            for play in tie:
                if play[0] == line[0]:
                    score += int(play[2]) + 3
                    break
        elif line[2] == "Z":
            for play in win:
                if play[0] == line[0]:
                    score += int(play[2]) + 6
                    break
        # print(score)
    print(score)
