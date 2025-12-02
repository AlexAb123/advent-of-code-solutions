from pathlib import Path
import copy
lines = Path(__file__).with_name('day 14 input.txt').open('r').read().strip().split("\n")

rocks = set()
cubeRocks = set()

for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] == "O":
            rocks.add((r,c))
        elif lines[r][c] == "#":
            cubeRocks.add((r,c))

def getNextPos(rock):
    row = rock[0]
    col = rock[1]
    check = []
    for r in rocks:
        if r[1] == col:
            check.append(r)
    for r in cubeRocks:
        if r[1] == col:
            check.append(r)
    m = -1
    for r in check:
        if r[0] < row and r[0] > m:
            m = r[0]

    return m + 1

def translateRocks():
    for row in range(len(lines[0])):
        for rock in rocks:
            if rock[0] == row:
                p = (getNextPos(rock), rock[1])
                rocks.remove(rock)
                rocks.add(p)

def rotate(rocks, cubeRocks):
    newRocks = set()
    newCubeRocks = set()
    for r in rocks:
        newRocks.add((r[1],len(lines)-r[0]-1))
    for r in cubeRocks:
        newCubeRocks.add((r[1],len(lines)-r[0]-1))
    return (newRocks, newCubeRocks)


cycles = []
translateRocks()

part1Score = 0
for rock in rocks:
    part1Score += len(lines) - rock[0]

originalRocks = copy.deepcopy(rocks)
prevRocks = set()
done = False
i = 0
index = 0
while not done:
    for turn in range(4):
        rocks, cubeRocks = rotate(rocks, cubeRocks)
        prevRocks = rocks.copy()
        translateRocks()
    if rocks in cycles:
        index = cycles.index(rocks)
        done = True
    if rocks not in cycles:
        cycles.append(rocks)
    i+=1
i-=1
periodLength = i-index
periodStart = index
rocks = originalRocks
for cycle in range(((1000000000-periodStart)%(periodLength))+periodStart):
    for turn in range(4):
        rocks, cubeRocks = rotate(rocks, cubeRocks)
        prevRocks = copy.deepcopy(rocks)
        part2Score = 0
        for rock in prevRocks:
            part2Score += len(lines) - rock[0]
        translateRocks()
    if rocks in cycles:
        done = True
    if rocks not in cycles:
        cycles.append(rocks)

part2Score = 0
for rock in prevRocks:
    part2Score += len(lines) - rock[0]
print(f"Part 1: {part1Score}\nPart 2: {part2Score}")