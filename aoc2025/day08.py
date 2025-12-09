from math import dist, prod
from itertools import combinations
from collections import defaultdict

def solve(data):

    lines = list(map(lambda line: tuple(map(int, line.split(","))), data.split("\n")))

    parent = {}
    
    def find(x):
        if x not in parent: # If it's a new node, set its root to itself
            parent[x] = x
        if parent[x] != x: # If it's not its own root, set its parent to the root of its parent
            parent[x] = find(parent[x])
        return parent[x]
        
    def union(x, y):
        parent[find(x)] = find(y)
        
    connections = sorted(combinations(lines, 2), key=lambda p: dist(*p))
    
    edges = 0
    for i, (p1, p2) in enumerate(connections):
        
        if find(p1) != find(p2):
            union(p1, p2)
            edges += 1
            
        if i == 999: # If we are on the 1000th connection, part 1 is the product the sizes of the 3 largest circuits 
            sizes = defaultdict(int)
            for p in parent:
                sizes[find(p)] += 1
            part1 = prod(sorted(sizes.values(), reverse=True)[:3])
            
        if edges == len(lines) - 1: # If we have made every edge in the MST except for the last one, part2 is found
            part2 = p1[0] * p2[0]
            break

    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    data = (Path(__file__).parent/"inputs"/"day08.txt").read_text().strip()
    start = time()    
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")