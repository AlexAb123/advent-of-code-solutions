from collections import defaultdict
from pathlib import Path
lines = Path(__file__).with_name('day_03_input.txt').open('r').read().strip()

houses = defaultdict(int)

currentPos = [0, 0]
for direction in lines:
    if direction == ">":
        currentPos[0] += 1
    if direction == "<":
        currentPos[0] -= 1
    if direction == "^":
        currentPos[1] += 1
    if direction == "v":
        currentPos[1] -= 1
    houses[tuple(currentPos)] += 1
print(f"Part 1: {len(houses)}")

houses = defaultdict(int)
santaPos = [0, 0]
roboSantaPos = [0, 0]
houses[tuple(santaPos)] += 1
for i, direction in enumerate(lines):
    if i % 2 == 0:
        if direction == ">":
            santaPos[0] += 1
        if direction == "<":
            santaPos[0] -= 1
        if direction == "^":
            santaPos[1] += 1
        if direction == "v":
            santaPos[1] -= 1
        houses[tuple(santaPos)] += 1
    else:
        if direction == ">":
            roboSantaPos[0] += 1
        if direction == "<":
            roboSantaPos[0] -= 1
        if direction == "^":
            roboSantaPos[1] += 1
        if direction == "v":
            roboSantaPos[1] -= 1
        houses[tuple(roboSantaPos)] += 1
print(f"Part 2: {len(houses)}")
