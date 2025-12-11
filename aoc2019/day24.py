from copy import deepcopy

def solve(data):

    layout = list(map(list, data.split("\n")))

    part1 = part2 = 0

    def biodiversity(layout):
        power = 0
        total = 0
        for r in range(len(layout)):
            for c in range(len(layout[0])):
                if layout[r][c] == "#":
                    total += 2 ** power
                power += 1
        return total
        
    def adjs(r, c):
        for dr, dc in (1, 0), (-1, 0), (0, 1), (0, -1):
            yield (r + dr, c + dc)
        
    seen = set()
    while tuple(map(tuple, layout)) not in seen:
        seen.add(tuple(map(tuple, layout)))
        new_layout = deepcopy(layout)
        for r in range(len(layout)):
            for c in range(len(layout[0])):
                bugs = 0
                for ar, ac in adjs(r, c):
                    if not (0 <= ar < len(layout) and 0 <= ac < len(layout[0])):
                        continue
                    if layout[ar][ac] == "#":
                        bugs += 1
                if layout[r][c] == "#":
                    if bugs != 1:
                        new_layout[r][c] = "."
                else:
                    if bugs == 1 or bugs == 2:
                        new_layout[r][c] = "#"
                        
        layout = new_layout
    part1 = biodiversity(layout)
    for i in layout:
        print("".join(i))
    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    data = (Path(__file__).parent/"inputs"/"day24.txt").read_text().strip()
    start = time()
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")