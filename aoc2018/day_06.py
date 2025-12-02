from pathlib import Path

def solve():

    from collections import defaultdict
    positions = [list(map(int, line.split(", "))) for line in Path(__file__).with_name('day_06_input.txt').open('r').read().strip().split("\n")]

    nodes = {pos[0]+pos[1]*1j for pos in positions}

    min_row = int(min(nodes, key=lambda x: x.real).real)
    max_row = int(max(nodes, key=lambda x: x.real).real)
    min_col = int(min(nodes, key=lambda x: x.imag).imag)
    max_col = int(max(nodes, key=lambda x: x.imag).imag)

    def find_closest_node(pos):
        return min(nodes, key=lambda x: abs(x.real - pos.real)+abs(x.imag-pos.imag))

    infinite_areas = set()
    for r in (min_row, max_row):
        for c in (min_col, max_col):
            infinite_areas.add(find_closest_node(r+c*1j))
    areas = defaultdict(int)
    for r in range(min_row, max_row+1):
        for c in range(min_col, max_col+1):
            pos = r+c*1j
            closest_node = find_closest_node(pos)
            if closest_node not in infinite_areas:
                areas[closest_node] += 1
    part1 = max(areas.values())

    part2 = 0
    for r in range(min_row, max_row+1):
        for c in range(min_col, max_col+1):
            pos = r+c*1j
            total_dist = 0
            for node in nodes:
                total_dist += int(abs(node.real - pos.real) + abs(node.imag - pos.imag))
                if total_dist >= 10000:
                    break
            if total_dist < 10000:
                part2 += 1

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")