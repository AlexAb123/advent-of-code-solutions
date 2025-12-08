from math import dist, prod
from itertools import combinations

def solve(data):

    lines = list(map(lambda line: tuple(map(int, line.split(","))), data.split("\n")))

    parent = {}
    size = {} # Call using size(find(x))

    def find(x):
        if x not in parent: # If it'sd a new node, set its root to itself and it's size to 1
            parent[x] = x
            size[x] = 1
        if parent[x] != x: # If it's not its own root, set its parent to the root of its parent
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rootx, rooty, = find(x), find(y)
        if rootx != rooty: # If they are in different sets, union them and add their sizes
            parent[rooty] = rootx
            size[rootx] += size.pop(rooty)

    connections = sorted(combinations(lines, 2), key=lambda p: dist(*p))
    
    for i, (p1, p2) in enumerate(connections):
        union(p1, p2)
        if size[find(p1)] >= len(lines):
            break
        if i == 1000:
            part1 = prod(sorted(size.values(), reverse=True)[:3])
    part2 = p1[0] * p2[0]

    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    data = (Path(__file__).parent/"inputs"/"day08.txt").read_text().strip()
    start = time()    
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")