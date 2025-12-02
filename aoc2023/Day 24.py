from pathlib import Path
import numpy as np
import sympy as sp
from sympy.abc import x, y, z, t
import time

startTime = time.time()
lines = Path(__file__).with_name('day 24 input.txt').open('r').read().strip().split("\n")
lines = [line.split(" @ ") for line in lines]
for i in range(len(lines)):
    for j in range(len(lines[0])):
        lines[i][j] = lines[i][j].split(", ")
for i in range(len(lines)):
    for j in range(len(lines[0])):
        for k in range(len(lines[0][0])):
            lines[i][j][k] = int(lines[i][j][k])


def findIntersection2D(line1, line2):

    slope1 = line1[1][1]/line1[1][0]
    slope2 = line2[1][1]/line2[1][0]

    if slope1 == slope2:
        return [[-1], [-1]]

    b1 = line1[0][1] - (line1[0][0]*slope1)
    b2 = line2[0][1] - (line2[0][0]*slope2)

    A = [[slope1, -1], [slope2, -1]]
    b = [[-b1], [-b2]]

    return np.linalg.solve(A ,b)

def isFuture(x, y, line):
    return not ((x < line[0][0] and line[1][0] > 0 or y < line[0][1] and line[1][1] > 0) or (x > line[0][0] and line[1][0] < 0 or y > line[0][1] and line[1][1] < 0))

testArea = (200000000000000, 400000000000000)
part1Score = 0

for i in range(len(lines)):

    for j in range(i+1, len(lines)):
        xx, yy = findIntersection2D(lines[i], lines[j])
        if testArea[0] <= xx[0] <= testArea[1] and testArea[0] <= yy[0] <= testArea[1] and isFuture(xx[0], yy[0], lines[i]) and isFuture(xx[0], yy[0], lines[j]):
            part1Score += 1

print(f"Part 1: {part1Score}")
print(f"Time Part 1: {time.time()-startTime}")

startTime = time.time()
possiblevx = set()
possiblevy = set()
possiblevz = set()
for ix in range(-300,300):
    possiblevx.add(ix)
for iy in range(-300,300):
    possiblevy.add(iy)
for iz in range(-300,300):
    possiblevz.add(iz)
done = False
for rockvx in possiblevx:
    for rockvy in possiblevy:
        equations = []
        ts = []
        for i, line in enumerate(lines[:3]):
            xp,yp,zp = line[0]
            vx,vy,vz = line[1]
            vx -= rockvx
            vy -= rockvy
            t = sp.symbols(f"t{i}")

            equations.append(xp+vx*t-x)
            equations.append(yp+vy*t-y)
            ts.append(t)

        solution = sp.solve(equations, x, y, *ts, dict=True)
        if len(solution) != 0:
            for rockvz in possiblevz:
                equations = []
                ts = []
                for i, line in enumerate(lines[:3]):
                    xp,yp,zp = line[0]
                    vx,vy,vz = line[1]
                    vx -= rockvx
                    vy -= rockvy
                    vz -= rockvz
                    t = sp.symbols(f"t{i}")

                    equations.append(xp+vx*t-x)
                    equations.append(yp+vy*t-y)
                    equations.append(zp+vz*t-z)
                    ts.append(t)

                solution = sp.solve(equations, x, y, z, *ts, dict=True)
                if len(solution) != 0:
                    print(f"Part 2: {solution[0][x]+solution[0][y]+solution[0][z]}")
                    print(f"Time Part 2: {time.time()-startTime}")
                    done = True
                    break