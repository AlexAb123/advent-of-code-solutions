from pathlib import Path
from collections import defaultdict
lines = Path(__file__).with_name('03_input.txt').open('r').read().strip().split('\n')
lines = [lines[0].split(','), lines[1].split(',')]

directions = {'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0)}

wire1 = set()
wire2 = set()

current = (0, 0)
for instruction in lines[0]:
    for i in range(int(instruction[1:])):
        current = (current[0] + directions[instruction[0]][0], current[1] + directions[instruction[0]][1])
        wire1.add(current)
current = (0, 0)
for instruction in lines[1]:
    for i in range(int(instruction[1:])):
        current = (current[0] + directions[instruction[0]][0], current[1] + directions[instruction[0]][1])
        wire2.add(current)

intersections = set()
for point in wire1:
    if point in wire2:
        intersections.add(point)
closestIntersection = min(intersections, key=lambda p: abs(p[0]) + abs(p[1]))
print(f'Part 1: {abs(closestIntersection[0]) + abs(closestIntersection[1])}')

current = (0, 0)
steps = 0
wire1Intersections = {}
for instruction in lines[0]:
    for i in range(int(instruction[1:])):
        current = (current[0] + directions[instruction[0]][0], current[1] + directions[instruction[0]][1])
        steps += 1
        if current in intersections:
            wire1Intersections[current] = steps
steps = 0
current = (0, 0)
wire2Intersections = {}
for instruction in lines[1]:
    for i in range(int(instruction[1:])):
        current = (current[0] + directions[instruction[0]][0], current[1] + directions[instruction[0]][1])
        steps += 1
        if current in intersections:
            wire2Intersections[current] = steps

intersectionSteps = set()
for intersection in wire1Intersections:
    intersectionSteps.add((wire1Intersections[intersection]+wire2Intersections[intersection], intersection))

print(f'Part 2: {min(intersectionSteps)[0]}')