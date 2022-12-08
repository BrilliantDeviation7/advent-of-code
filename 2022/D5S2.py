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
        stacks[int(l[5]) - 1] += stacks[int(l[3]) - 1][-int(l[1]):]
        stacks[int(l[3]) - 1] = stacks[int(l[3]) - 1][:len(stacks[int(l[3]) - 1]) - int(l[1])]
        # print(stacks)

for stack in stacks:
    print(stack[-1], end='')
