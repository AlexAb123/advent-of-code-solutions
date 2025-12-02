from pathlib import Path

def solve(): 
    import re
    from collections import defaultdict
    lines = [list(map(int, re.findall(r"-?\d+", line))) for line in Path(__file__).with_name('day_14_input.txt').open('r').read().strip().split("\n")]

    max_row, max_col = 103, 101

    for i in range(max_row * max_col):
        seen_positions = set()
        has_duplicate = False
        for line in lines:
            py, px, vy, vx = line
            pos = ((px+vx*i)%(max_row), (py+vy*i)%(max_col))
            if pos in seen_positions:
                has_duplicate = True
                break
            seen_positions.add(pos)

        if not has_duplicate:
            part2 = i
            break

    positions = defaultdict(int)
    for line in lines:
        py, px, vy, vx = line
        pos = ((px+vx*100)%(max_row), (py+vy*100)%(max_col))
        positions[pos] += 1

    quadrants = defaultdict(int)
    for pos, robots in positions.items():
        row, col = pos
        if row == max_row//2 or col == max_col//2:
            continue
        top, left = row < max_row//2, col < max_col//2
        quadrants[(top, left)] += robots

    part1 = 1
    for robots in quadrants.values():
        part1 *= robots

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")