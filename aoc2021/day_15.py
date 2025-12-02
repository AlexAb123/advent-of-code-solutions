from pathlib import Path

def solve():
        
    from heapq import heappush, heappop
    from collections import defaultdict
    lines = Path(__file__).with_name('day_15_input.txt').open('r').read().strip().split("\n")

    grid_part1 = {r+c*1j: int(lines[r][c]) for c in range(len(lines[0])) for r in range(len(lines))}
    rows, cols = len(lines), len(lines[0])
    grid_part2 = {}

    for r in range(len(lines)):
        for c in range(len(lines[0])):

            for dr in range(5):
                for dc in range(5):

                    grid_part2[(r+dr*rows)+(c*1j+(dc*cols*1j))] = int(lines[r][c]) + dr + dc
                    while grid_part2[(r+dr*rows)+(c*1j+(dc*cols*1j))] > 9:
                        grid_part2[(r+dr*rows)+(c*1j+(dc*cols*1j))] -= 9

    start = 0+0j
    end_part1 = len(lines) + len(lines[0])*1j -1-1j
    end_part2 = 5*(len(lines) + (len(lines[0]))*1j)-1-1j

    # i is to break ties because can't compare complex numbers

    def shortest_distance(start, end, grid):
        visited = set()
        q = [(0, -1, start)]
        distances = defaultdict(lambda: float('inf'))
        distances[start] = 0

        i = 0
        while q:

            dist, _, pos = heappop(q)

            for adj in (pos+1, pos-1, pos+1j, pos-1j):

                if adj not in grid:
                    continue

                if adj not in visited:

                    visited.add(adj)
                    
                    if grid[adj] + dist < distances[adj]:
                        distances[adj] = grid[adj] + dist

                    heappush(q, (distances[adj], i, adj))
                    i += 1

        return distances[end]

    part1 = shortest_distance(start, end_part1, grid_part1)
    part2 = shortest_distance(start, end_part2, grid_part2)
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")