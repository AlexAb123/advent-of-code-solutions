from pathlib import Path
lines = Path(__file__).with_name('day 21 input.txt').open('r').read().strip().split("\n")
import time

startTime = time.time()

rocks = set()
plots = set()
start = (0,0)

for row in range(len(lines)):
    for col in range(len(lines[0])):
        if lines[row][col] == "#":
            rocks.add((row, col))
        elif lines[row][col] == "S":
            start = (row, col)
        elif lines[row][col] == ".":
            plots.add((row, col))
plots.add(start)

def getAdjacents(pos):
    r, c = pos
    return [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]

def getWorldPosition(pos):
    return (pos[0]%len(lines), pos[1]%len(lines[0]))

current = None
currentDistance = 0
distances = {}
points = []
points.append([start])
temp = []

for i in range(64):
    temp = []
    for current in points[i]:

        for adj in getAdjacents(current):
            if getWorldPosition(adj) not in rocks:
                temp.append(adj)
    points.append(set(temp))
print(f"Part 1: {len(points[-1])}")

def getQuadratic(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    d = (x1-x2) * (x1-x3) * (x2-x3)
    a = (x3 * (y2-y1) + x2 * (y1-y3) + x1 * (y3-y2)) / d
    b = (x3*x3 * (y1-y2) + x2*x2 * (y3-y1) + x1*x1 * (y2-y3)) / d
    c = (x2 * x3 * (x2-x3) * y1+x3 * x1 * (x3-x1) * y2+x1 * x2 * (x1-x2) * y3) / d
    return (a, b, c)

points = []
points.append([start])
quadratic = []
x = (26501365-65)/131
a, b, c = 0, 0, 0
for i in range((131*3) + 65):
    temp = []
    for current in points[i]:
        for adj in getAdjacents(current):
            if getWorldPosition(adj) not in rocks:
                temp.append(adj)
    points.append(set(temp))

    if ((i+1)-65)%131 == 0:
        quadratic.append((((i+1)-65)//131, len(points[-1])))
    if len(quadratic) >= 3:
        j = (((i+1)-65)//131)-2
        newA, newB, newC = getQuadratic(quadratic[j], quadratic[j+1], quadratic[j+2])
        if newA == a and newB == b and newC == c:
            break
        else:
            a = newA
            b = newB
            c = newC

print(f"Part 2: {int((a*(x**2))+(b*x)+c)}")
print(f"Time Taken: {(time.time() - startTime)**100//1/100}")