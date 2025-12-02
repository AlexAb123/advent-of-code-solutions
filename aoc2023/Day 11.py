from pathlib import Path

lines = Path(__file__).with_name('day 11 input.txt').open('r').read().strip().split("\n")
lines = [[lines[i][j] for j in range(len(lines[0]))] for i in range(len(lines))]

emptyRows = set()
emptyColumns = set()
for r in range(len(lines)):
    hasGalaxy = False
    for c in range(len(lines[0])):
        if lines[r][c] == "#":
            hasGalaxy = True
            break
    if not hasGalaxy:
        emptyRows.add(r)
for c in range(len(lines[0])):
    hasGalaxy = False
    for r in range(len(lines)):
        if lines[r][c] == "#":
            hasGalaxy = True
            break
    if not hasGalaxy:
        emptyColumns.add(c)

galaxies = []
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "#":
            galaxies.append([i,j])

part1Score = 0
part2Score = 0
part1Expansion = 2
part2Expansion = 1000000

#Check every pair of galaxies
for i in range(len(galaxies)):
    for j in range(i+1,len(galaxies)):
        r1, c1 = galaxies[i]
        r2, c2 = galaxies[j]
        part1Score += abs(r1-r2) + abs(c1-c2)
        part2Score += abs(r1-r2) + abs(c1-c2)
        for r in emptyRows:
            if min(r1, r2) < r < max(r1, r2):
                part1Score += part1Expansion - 1
                part2Score += part2Expansion - 1
        for c in emptyColumns:
            if min(c1, c2) < c < max(c1, c2):
                part1Score += part1Expansion - 1
                part2Score += part2Expansion - 1

print(f"Part 1: {part1Score}\nPart 2: {part2Score}")