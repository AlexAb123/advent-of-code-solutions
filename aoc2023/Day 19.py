from pathlib import Path
from collections import defaultdict
from copy import deepcopy
lines = Path(__file__).with_name('day 19 input.txt').open('r').read().strip().split("\n\n")

wor = lines[0].split("\n")
rat = lines[1].split("\n")
workflows = defaultdict(list)

for x in wor:
    j = x.split("{")
    for i in j[1][:-1].split(","):
        y = i.split(":")
        if len(y) == 2:
            workflows[j[0]].append([y[0][0], y[0][1], int(y[0][2:]), y[1]])
        else:
            workflows[j[0]].append(y)

accepted = set()
ratings = []
for r in rat:
    x = r.split(",")
    temp = []
    for j in x:
        temp.append(int(j.replace("}", "").split("=")[1]))
    ratings.append(temp)

# x, m, a, s
xmas = {"x":0, "m":1, "a":2, "s":3}
def isAcceptedAndScore(part, work="in"):

    if work == "A":
        return sum(part)
    if work == "R":
        return 0

    for w in workflows[work]:
        if len(w) == 1:
            return isAcceptedAndScore(part, w[0])
        else:
            val, op, num, nextw = w
            if op == "<":
                if part[xmas[val]] < num:
                    return isAcceptedAndScore(part, nextw)
            elif op == ">":
                if part[xmas[val]] > num:
                    return isAcceptedAndScore(part, nextw)
def splitRange(partRange, op, val, num):
    valIndex = xmas[val]
    r1 = deepcopy(partRange)
    r2 = deepcopy(partRange)
    ret = []
    if partRange[valIndex][0] <= num < partRange[valIndex][1]:
        if op == "<":
            r1[valIndex][1] = num
            r2[valIndex][0] = num
            ret.append(r1)
            ret.append(r2)

        elif op == ">":
            r1[valIndex][0] = num+1
            r2[valIndex][1] = num+1
            ret.append(r1)
            ret.append(r2)
    return ret


def getValidCombos(partRanges=[[1, 4001] for i in range(4)], work="in"):
    total = 0
    if work == "A":
        combos = 1
        for r in partRanges:
            combos *= r[1]-r[0]
        return combos

    if work == "R":
        return 0
    for w in workflows[work]:
        if len(w) == 1:
            total += getValidCombos(partRanges, w[0])
        else:
            val, op, num, nextw = w
            newRange, partRanges = splitRange(partRanges, op, val, num)
            total += getValidCombos(newRange, nextw)
    
    return total

part1Score = 0
for rating in ratings:
    part1Score += isAcceptedAndScore(rating)
print(f"Part 1: {part1Score}")
print(f"Part 2: {getValidCombos()}")