from pathlib import Path
lines = Path(__file__).with_name('day_01_input.txt').open('r').read().strip()

currentFloor = 0
part2 = 0
found = False
for i, x in enumerate(lines):
    currentFloor += 1 if x == "(" else -1
    if currentFloor == -1 and not found:
        part2 = i + 1
        found = True
part1 = currentFloor
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")