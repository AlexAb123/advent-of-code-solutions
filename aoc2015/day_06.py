from pathlib import Path
from collections import defaultdict
lines = [((v := line.split(" "))[:-2] + v[-1:] if len(v := line.split(" ")) == 4 else v[1:-2] + v[-1:]) for line in Path(__file__).with_name('day_06_input.txt').open('r').read().strip().split("\n")]
lines = [[line[0], list(map(int,line[1].split(","))), list(map(int,line[2].split(",")))] for line in lines]

part1Grid = defaultdict(bool)
part2Grid = defaultdict(int)
for line in lines:
    for x in range(line[1][0], line[2][0]+1):
        for y in range(line[1][1], line[2][1]+1):
            if line[0] == "on":
                part1Grid[(x,y)] = True
                part2Grid[(x,y)] += 1
            elif line[0] == "off":
                part1Grid[(x,y)] = False
                part2Grid[(x,y)] = max(0, part2Grid[(x,y)]-1)
            elif line[0] == "toggle":
                part1Grid[(x,y)] = not part1Grid[(x,y)]
                part2Grid[(x,y)] += 2

part1 = 0
for value in part1Grid.values():
    if value:
        part1 += 1
print(f"Part 1: {part1}")

part2 = 0
for value in part2Grid.values():
    part2 += value
print(f"Part 2: {part2}")