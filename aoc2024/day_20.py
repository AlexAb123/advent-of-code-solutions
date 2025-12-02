from pathlib import Path

def solve():
    
    lines = Path(__file__).with_name('day_20_input.txt').open('r').read().strip().split("\n")

    start = None
    tracks = set()
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == "#":
                continue
            elif lines[r][c] == "S":
                start = r+c*1j
            tracks.add(r+c*1j)

    path = []
    visited = set()
    stack = [start]
    dists = {}
    dist = 0
    while stack:
        curr = stack.pop()
        path.append(curr)
        visited.add(curr)
        dists[curr] = dist
        for adj in curr+1, curr-1, curr+1j, curr-1j:
            if adj not in visited and adj in tracks:
                stack.append(adj)
                dist += 1

    part1, part2 = 0, 0
    max_cheats = 20

    window = set()
    curr = path[0]
    for dr in range(-max_cheats, max_cheats+1):
        for dc in range(-max_cheats+abs(dr), max_cheats-abs(dr)+1):
            window.add(dr+dc*1j)

    for i in range(len(path)):
        curr = path[i]
        for d in window:
            manhattan_dist = int(abs(d.real)+abs(d.imag))
            if curr+d in visited and dists[curr] - dists[curr+d] - manhattan_dist >= 100:
                part2 += 1
                if manhattan_dist <= 2:
                    part1 += 1

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")