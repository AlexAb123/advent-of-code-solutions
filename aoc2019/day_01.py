from pathlib import Path
lines = map(int, Path(__file__).with_name('01_input.txt').open('r').read().strip().split("\n"))

def getFuel(fuel):
    if fuel <= 0:
        return 0
    return fuel + getFuel(fuel//3-2)

part1Score = 0
part2Score = 0
for line in lines:
    part1Score += line//3-2
    part2Score += getFuel(line//3-2)

print(f"Part 1: {part1Score}")
print(f"Part 2: {part2Score}")