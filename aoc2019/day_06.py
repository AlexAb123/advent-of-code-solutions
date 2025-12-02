from pathlib import Path
from collections import defaultdict
import heapq
lines = Path(__file__).with_name('06_input.txt').open('r').read().strip().split("\n")
lines = [line.split(")") for line in lines]

orbits = {}
adjacents = defaultdict(list)
for line in lines:
    orbits[line[1]] = line[0]
    adjacents[line[0]].append(line[1])
    adjacents[line[1]].append(line[0])

def getDepth(currentPlanet, depth=0):
    if currentPlanet not in orbits:
        return depth
    return getDepth(orbits[currentPlanet], depth+1)

part1Score = 0
for planet in orbits:
    part1Score += getDepth(planet)
print(f"Part 1: {part1Score}")

q = [("YOU", 0)]
visited = set()
while q:
    current, currentDistance = q.pop(0)
    visited.add(current)
    if current == "SAN":
        break
    for adj in adjacents[current]:
        if adj not in visited:
            q.append((adj, currentDistance + 1))

print(f"Part 2: {currentDistance-2}")