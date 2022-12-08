stacks = list(map(list, [
    "SZPDLBFC",
    "NVGPHWB",
    "FWBJG",
    "GJNFLWCS",
    "WJLTPMSH",
    "BCWGFS",
    "HTPMQBW",
    "FSWT",
    "NCR",
]))

with open('D5_input.txt', 'r') as f:
    for l in f:
        l = l[:-1].split()
        for i in range(int(l[1])):
            stacks[int(l[5]) - 1].append(stacks[int(l[3]) - 1].pop())
        # print(stacks)

for stack in stacks:
    print(stack[-1], end='')
