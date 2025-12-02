from pathlib import Path

def solve():

    from collections import defaultdict
    from heapq import heappop, heappush

    lines = Path(__file__).with_name('day_16_input.txt').open('r').read().strip().split("\n")

    walls = set()
    start = None
    end = None
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == "#":
                walls.add(r+c*1j)
            elif lines[r][c] == "S":
                start = r+c*1j
            elif lines[r][c] == "E":
                end = r+c*1j

    def get_adjs(current):
        pos, d = current
        if pos+d not in walls:
            yield ((pos+d, d), 1)
        yield ((pos, 1j*d), 1000)
        yield ((pos, -1j*d), 1000)

    # Dijkstra's Algorithm with a special case if ajj_dist + dist == distances[adj]
    visited = set()
    dists = defaultdict(lambda: float('inf'))
    dists[(start, 1j)] = 0
    pq = [(0, -1, (start, 1j))]
    parents = defaultdict(set)
    key = 0
    while pq:

        dist, _, curr = heappop(pq)

        for adj, adj_dist in get_adjs(curr):

            if adj_dist + dist < dists[adj]:
                dists[adj] = adj_dist + dist
                parents[adj] = {curr}

            elif adj_dist + dist == dists[adj]:
                parents[adj].add(curr)

            if adj not in visited:
                visited.add(adj)
                heappush(pq, (dists[adj], key, adj))
                key += 1

    min_dist = min(dists[(end, d)] for d in (1,-1,1j,-1j))
    part1 = min_dist

    def get_unique_tiles_in_path(curr, unique_tiles):
        unique_tiles.add(curr[0])
        for parent in parents[curr]:
            unique_tiles.update(get_unique_tiles_in_path(parent, unique_tiles))
        return unique_tiles
    
    unique_tiles = set()
    for curr in ((end, d) for d in (1,-1,1j,-1j)):
        if dists[curr] != min_dist:
            continue
        unique_tiles.update(get_unique_tiles_in_path(curr, set()))

    part2 = len(unique_tiles)

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")