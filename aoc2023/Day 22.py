from pathlib import Path
from collections import defaultdict
lines = Path(__file__).with_name('day 22 input.txt').open('r').read().strip().split("\n")
lines = [line.split("~") for line in lines]
lines = [[list(map(int, pos.split(","))) for pos in line] for line in lines]


def overlapRange(range1, range2):
    s1, e1 = min(range1), max(range1)
    s2, e2 = min(range2), max(range2)
    return s1 <= e2 and e1 >= s2

def overlapHorizontal(range1, range2):
    xrange1 = (range1[0][0], range1[1][0])
    yrange1 = (range1[0][1], range1[1][1])
    xrange2 = (range2[0][0], range2[1][0])
    yrange2 = (range2[0][1], range2[1][1])

    return overlapRange(xrange1, xrange2) and overlapRange(yrange1, yrange2)

lines = sorted(lines, key=lambda x: (min(x[0][2], x[1][2])))

for i in range(len(lines)):
    currentMax = 0
    found = False
    for j in range(len(lines)):
        if i != j and overlapHorizontal(lines[i], lines[j]) and lines[j][1][2] > currentMax and lines[j][1][2] < lines[i][0][2]:
            currentMax = lines[j][1][2]
            found = True
    if found:
        fallHeight = lines[i][0][2] - currentMax
        lines[i][0][2] = lines[i][0][2] - fallHeight + 1
        lines[i][1][2] = lines[i][1][2] - fallHeight + 1
    else:
        fallHeight = lines[i][0][2] - 0
        lines[i][0][2] = lines[i][0][2] - fallHeight + 1
        lines[i][1][2] = lines[i][1][2] - fallHeight + 1
lines = sorted(lines, key=lambda x: (min(x[0][2], x[1][2])))

supports = defaultdict(set)
for i in range(len(lines)):
    if min(lines[i][0][2], lines[i][1][2]) == 1:
        supports[-1].add(i)

for i in range(len(lines)):
    supports[i] = set()

for i in range(len(lines)):
    for j in range(i-1, -2, -1):
        if overlapHorizontal(lines[i], lines[j]):
            if min(lines[i][0][2], lines[i][1][2]) - max(lines[j][0][2], lines[j][1][2]) == 1:
                supports[j].add(i)

def countNotSupported(supports):
    allRocks = [i for i in range(len(lines))]
    for v in supports.values():
        for j in v:
            if j in allRocks:
                allRocks.remove(j)
    return len(allRocks)

removed = 0
for i in range(len(lines)):
    tempSupports = supports.copy()
    tempSupports[i] = set()
    if countNotSupported(tempSupports) == 0:
        removed += 1
print(f"Part 1: {removed}")

def notSupported(brick, supports):
    for v in supports.values():
        if brick in v:
            return False
    return True

def countFallenBricks(brick):
    
    q = []
    q.append(brick)
    toRemove = set()
    tempSupports = supports.copy()

    while q:

        current = q.pop(0)
        tempSupports[current] = set()

        for supporting in supports[current]:
            if supporting not in toRemove and notSupported(supporting, tempSupports):
                q.append(supporting)
                toRemove.add(supporting)

    return len(toRemove)

part2Score = 0 
for i in range(len(lines)):
    part2Score += countFallenBricks(i)
print(f"Part 2: {part2Score}")