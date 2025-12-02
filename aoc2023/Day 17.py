from pathlib import Path
import heapq
from collections import defaultdict
import time
lines = Path(__file__).with_name('day 17 input.txt').open('r').read().strip().split("\n")

startTime = time.time()

edges = set()
for i in range(len(lines)):
    for j in range(len(lines[0])):
        for r in [-1,0,1]:
            for c in [-1,0,1]:
                if not (r!= 0 and c != 0) and not (r == 0 and c ==0) and 0 <= i+r < len(lines) and 0 <= j+c < len(lines[0]):
                    edges.add(((i, j),(i+r, j+c), int(lines[i+r][j+c])))

adjacents = defaultdict(list)
for edge in edges:
    adjacents[edge[0]].append((edge[1], edge[2]))

def getAdjacents(node, part1):
    if part1:
        ret = set()
        for adj in adjacents[node[0]]:
            d = (adj[0][0]-node[0][0], adj[0][1]-node[0][1])
            if d == node[1]:
                if node[2] + 1 <= 3:
                    ret.add(((adj[0], d, node[2]+1), adj[1]))
            else:
                ret.add(((adj[0], d, 1), adj[1]))
        return ret
    else:
        ret = set()
        for adj in adjacents[node[0]]:
            d = (adj[0][0]-node[0][0], adj[0][1]-node[0][1])
            if d == node[1]:
                if node[2] + 1 <= 10:
                    ret.add(((adj[0], d, node[2]+1), adj[1]))
            elif node[2] >= 4 or node[1] == (-1,-1):
                ret.add(((adj[0], d, 1), adj[1]))
        return ret

def getShortestDistance(part1):
    start = ((0,0), (-1,-1), 0)
    endPos = (len(lines)-1, len(lines[0])-1)
    heap = [(0,start)]
    distances = {}
    distances[start] = (0, None)
    while len(heap) > 0:
        currentDistance, current = heapq.heappop(heap)
        for neighbour, weight in getAdjacents(current, part1):
            newDistance = currentDistance + weight
            # Don't go back to a node (just the position of the node, not the other dimensions) if we were just on it.
            if distances[current][1] != None and neighbour[0] == distances[current][1][0]:
                continue
            # if unvisited, add to queue
            if neighbour not in distances:
                heapq.heappush(heap, (newDistance, neighbour))
            # if distance is infinity or if currentDistance is less, then update distance
            if neighbour not in distances or newDistance < distances[neighbour][0]:
                distances[neighbour] = (newDistance, current)
    scores = set()
    for node, dist in distances.items():
        if node[0] == endPos:
            scores.add(dist[0])
    return min(scores)

print(f"Part 1: {getShortestDistance(True)}")
print(f"Time Taken: {(time.time() - startTime)*100//1/100}\n")
startTime = time.time()
print(f"Part 2: {getShortestDistance(False)}")
print(f"Time Taken: {(time.time() - startTime)*100//1/100}")