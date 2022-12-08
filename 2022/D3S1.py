import string


def priority(c): return string.ascii_letters.find(c) + 1


prioritiesSum = 0
with open('D3_input.txt', 'r') as f:
    for l in f:
        l = l.split('\n')[0]
        compartment1 = l[:len(l) // 2]
        compartment2 = l[len(l) // 2:]
        for i, v in enumerate(compartment1):
            if v in compartment2:
                prioritiesSum += priority(v)
                break
print(prioritiesSum)
