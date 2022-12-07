import pprint


def getDir(a, dirs):
    d = a[dirs[0]]
    for i in range(1, len(dirs)):
        d = d[dirs[i]]
    return d


def recurSum(n):
    sum = 0
    for key in n:
        if not isinstance(n[key], dict):
            sum += n[key]
        else:
            sum += recurSum(n[key])
    return sum


with open('D7_input.txt', 'r') as f:
    cmds = []
    for l in f:
        cmds.append(l.split())

    r = {"root": {}}
    dirs = ["root"]

    sums = []
    for i in cmds:
        if i[0].isnumeric():
            getDir(r, dirs)[i[1]] = int(i[0])
        elif i[0] == "dir":
            if not getDir(r, dirs).get(i[1]):
                getDir(r, dirs)[i[1]] = {}
        elif i[1] == "cd" and i[2] != "/":
            if i[2] == "..":
                dirSum = recurSum(getDir(r, dirs))
                sums.append(dirSum)
                dirs.pop()
            else:
                dirs.append(i[2])

    for x in range(len(dirs) - 1, 0, -1):
        dirSum = recurSum(getDir(r, dirs[:x + 1]))
        sums.append(dirSum)

    minDelete = recurSum(r)
    target = 30000000 - (70000000 - minDelete)
    sums = [z for z in sums if z < minDelete and z >= target]
    print(min(sums))
