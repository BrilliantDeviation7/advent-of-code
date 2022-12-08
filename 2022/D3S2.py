import string


def priority(c): return string.ascii_letters.find(c) + 1


prioritiesSum = 0
with open('D3_input.txt', 'r') as f:
    lines = [line.replace('\n', '') for line in f.readlines()]
    for i in range(len(lines) // 3):
        rucksack1 = lines[3 * i]
        rucksack2 = lines[3 * i + 1]
        rucksack3 = lines[3 * i + 2]
        for i, v in enumerate(rucksack1):
            if v in rucksack2 and v in rucksack3:
                prioritiesSum += priority(v)
                break
print(prioritiesSum)
