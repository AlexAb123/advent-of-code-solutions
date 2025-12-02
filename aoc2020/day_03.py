from pathlib import Path
lines = Path(__file__).with_name('day_03_input.txt').open('r').read().strip().split("\n")

trees = set()
for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] == "#":
            trees.add((r,c))

slopes = [(1, 3), (1,1), (1,5), (1,7), (2,1)]
start = (0, 0)
totalTrees = []
for slope in slopes:
    current = start
    treesEncountered = 0
    while current[0] < len(lines):
        if (current[0]%len(lines), current[1]%len(lines[0])) in trees:
            treesEncountered += 1
        current = (current[0]+slope[0], current[1]+slope[1])
    totalTrees.append(treesEncountered)
print(f"Part 1: {totalTrees[0]}")
part2Score = 1
for t in totalTrees:
    part2Score *= t
print(f"Part 2: {part2Score}")
