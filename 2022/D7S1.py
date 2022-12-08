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
    cmds = [l.split() for l in f.readlines()]
    r = {"root": {}}
    dirs = ["root"]

    sum = 0
    for i in cmds:
        # print(i)
        if i[0].isnumeric():
            getDir(r, dirs)[i[1]] = int(i[0])
        elif i[0] == "dir":
            if not getDir(r, dirs).get(i[1]):
                getDir(r, dirs)[i[1]] = {}
        elif i[1] == "cd" and i[2] != "/":
            if i[2] == "..":
                dirSum = recurSum(getDir(r, dirs))
                # print(f"Calculated directory {dirs[-1]}'s size:", dirSum)
                if dirSum <= 100000:
                    sum += dirSum
                dirs.pop()
            else:
                dirs.append(i[2])

    # had to add this part for when the last directories are not exited out of with cd ..
    # must go through last directories remaining in the list

    for x in range(len(dirs) - 1, 0, -1):
        dirSum = recurSum(getDir(r, dirs[:x + 1]))
        if dirSum <= 100000:
            sum += dirSum

    # pprint.pprint(r)
    print(sum)
