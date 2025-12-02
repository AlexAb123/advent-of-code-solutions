from pathlib import Path
from collections import defaultdict
import time
lines = Path(__file__).with_name('day 23 input.txt').open('r').read().strip().split("\n")

startTime = time.time()

rightSlopes = set()
downSlopes = set()
empty = set()

for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] == "v":
            downSlopes.add((r,c))
            empty.add((r,c))
        elif lines[r][c] == ">":
            rightSlopes.add((r,c))
            empty.add((r,c))
        elif lines[r][c] == ".":
            empty.add((r,c))

def getAdjacentsPart1(pos):
    r, c = pos
    if pos in downSlopes:
        return [(r+1,c)]
    if pos in rightSlopes:
        return [(r,c+1)]
    return [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]


def DFS1(current, target, visited, distance=0):
    longest = distance

    if current == target:
        return longest
    
    visited.add(current)
    for adj in getAdjacentsPart1(current):
        if adj not in visited and adj in empty:
            longest = max(longest, DFS1(adj, target, visited.copy(), distance+1))
    return longest

connections = defaultdict(list)
for pos in empty:
    r, c = pos
    for adj in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
        if adj in empty:
            connections[pos].append([adj, 1])

def getNextCorners(pos, connections):
    corners = []
    for adj in connections[pos]:
        q = [adj[0]]
        current = None
        steps = 0
        visited = set()
        visited.add(pos)
        while len(connections[current]) == 2 or current == None:
            current = q.pop(0)
            visited.add(current)
            steps += 1
            for a in connections[current]:
                if a[0] not in visited:
                    q.append(a[0])
        corners.append([current, steps])
    return corners

newConnections = defaultdict(list)
for pos, adjacents in connections.copy().items():
    if len(adjacents) != 2 and pos not in newConnections:
        for n in getNextCorners(pos, connections):
            newConnections[pos].append(n)
start = (0,1)
end = (len(lines)-1, len(lines[0])-2)
for k,v in newConnections.copy().items():
    for i in v:
        if i[0] == start:
            newConnections[k].remove(i)
connections = newConnections

def DFS2(current, target, visited, connections, secondToLast, distance=0):
    longest = distance
    
    if current == target:
        return longest
    visited.add(current)

    if current == secondToLast:
        longest = max(longest, DFS2(end, target, visited.copy(), connections, secondToLast, distance+connections[end][0][1]))
        return longest

    for adj in connections[current]:
        if adj[0] not in visited:
            longest = max(longest, DFS2(adj[0], target, visited.copy(), connections, secondToLast, distance+adj[1]))
    return longest

import sys
sys.setrecursionlimit(3000)

print(f"Part 1: {DFS1(start, end, set())}")
print(f"Part 1 Time Taken: {(time.time()-startTime)*100//1/100}")
secondToLast = connections[end][0][0]
startTime = time.time()
print(f"Part 2: {DFS2(start, end, set(), connections, secondToLast)}")
print(f"Part 2 Time Taken: {(time.time()-startTime)*100//1/100}")