from pathlib import Path
from collections import Counter

lines = Path(__file__).with_name('day_02_input.txt').open('r').read().strip().split("\n")
lines = [line.split(" ") for line in lines]
lines = [[list(map(int, line[0].split("-"))), line[1][0], line[2]] for line in lines]

part1Score = 0
part2Score = 0
for line in lines:
    count = Counter(line[2])[line[1]]
    if line[0][0] <= count <= line[0][1]:
        part1Score += 1
    if (line[2][line[0][0]-1] == line[1]) != (line[2][line[0][1]-1] == line[1]):
        part2Score += 1
print(f"Part 1: {part1Score}")
print(f"Part 2: {part2Score}")