from pathlib import Path
from collections import defaultdict
import time
import random
from copy import deepcopy
lines = Path(__file__).with_name('day 25 input.txt').open('r').read().strip().split("\n")

startTime = time.time()

edges = []
for line in lines:
    split = line.split(':')
    for comp in split[1][1:].split(' '):
        edges.append([split[0], comp])

def countNodes(edges):
    nodes = set()
    for edge in edges:
        nodes.add(edge[0])
        nodes.add(edge[1])
    return len(nodes)

def contract(edges, node1, node2):
    for i in range(len(edges)-1, -1, -1):
        if (edges[i][0] == node1 and edges[i][1] == node2) or (edges[i][0] == node2 and edges[i][1] == node1):
            edges.remove(edges[i])
        elif edges[i][0] == node1 or edges[i][0] == node2:
            edges[i][0] = node1 + ", " + node2
        elif edges[i][1] == node1 or edges[i][1] == node2:
            edges[i][1] = node1 + ", " + node2
    return edges

def karger(edges):
    while countNodes(edges) > 2:
        toRemove = random.choice(edges)
        edges.remove(toRemove)
        edges = contract(edges, toRemove[0], toRemove[1])
    return edges

karg = []
while len(karg) != 3:
    karg = karger(deepcopy(edges))
print(f'Part 1 AND 2: {len(karg[0][0].split(","))*len(karg[0][1].split(","))}')
print(f'Time Taken: {(time.time()-startTime)*100//1/100}')