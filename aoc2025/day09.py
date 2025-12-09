from itertools import combinations
from collections import defaultdict

def solve(data):

    lines = list(map(lambda line: tuple(map(int, line.split(",")[::-1])), data.split("\n")))
    combos = list(combinations(lines, 2))
    part1 = max((abs(r1 - r2) + 1) * (abs(c1 - c2) + 1) for (r1, c1), (r2, c2) in combos)
    
    tiles = defaultdict(set)
    all_tiles = set(lines)
    
    for r, c in lines:
        tiles[r].add((r, c))
    for i in range(len(lines)):
        (r1, c1), (r2, c2) = lines[i], lines[(i + 1)%len(lines)]
        if r1 == r2:
            for c in range(min(c1, c2), max(c1, c2)+1):
                tiles[r1].add((r1, c))
                all_tiles.add((r1, c))
                
        else:
            for r in range(min(r1, r2), max(r1, r2) + 1):
                tiles[r].add((r, c1))
                all_tiles.add((r, c1))
    
    min_r = min(lines, key=lambda x: x[0])[0]
    max_r = max(lines, key=lambda x: x[0])[0]
        
    inside_ranges = defaultdict(list)
    for r in range(min_r, max_r + 1):
        row = sorted(tiles[r])
        inside = True
        for i in range(len(row) - 1):
            inside_ranges[r].append((row[i][1], row[i+1][1]))
            inside = not inside
    
    for r in inside_ranges:
        new_rangs = []
        new_rangs.append(inside_ranges[r].pop(0))
        for i in range(len(inside_ranges[r])):
            if new_rangs[-1][1] == inside_ranges[r][i][0]:
                new_rangs[-1] = (new_rangs[-1][0], inside_ranges[r][i][1])
            else:
                new_rangs.append(inside_ranges[r][i])
        inside_ranges[r] = new_rangs
    
    def valid_range(rang, inside_ranges):
        for r in inside_ranges:
            if rang[0] >= r[0] and rang[1] <= r[1]:
                return True
        return False
    
    possible = set()
    for p1, p2 in combos:
        r1, c1 = p1
        r2, c2 = p2

        found = True
        r_min, r_max = min(r1, r2), max(r1, r2)

        for r in range(r_min, r_max):
            rang = (min(c1, c2), max(c1, c2))
            if not valid_range(rang, inside_ranges[r]):
                found = False
                break
        if found:
            possible.add((abs(r1 - r2) + 1) * (abs(c1 - c2) + 1))

    part2 = max(possible)
        
    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    data = (Path(__file__).parent/"inputs"/"day09.txt").read_text().strip()
    start = time()
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")