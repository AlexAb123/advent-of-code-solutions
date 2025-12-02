from pathlib import Path
from collections import defaultdict

def solve():
    chunks = Path(__file__).with_name('day_20_input.txt').open('r').read().strip().split("\n\n")

    tiles = {}
    for chunk in chunks:
        lines = chunk.split("\n")
        tiles[int(lines[0][5:-1])] = lines[1:]

    def get_col(tile, c):
        col = []
        for row in tile:
            col.append(row[c])
        return col

    def get_sides(tile):
        for side in tile[0], tile[len(tile)-1], get_col(tile, 0), get_col(tile, len(tile[0])-1):
            yield side
            yield reversed(side)

    sides = defaultdict(set)
    for num, tile in tiles.items():
        for side in get_sides(tile):
            sides[num].add(tuple(side))

    matching_sides = defaultdict(int)
    for num in tiles.keys():
        for other_num, other_tile in tiles.items():
            if num == other_num:
                continue
            for side in sides[num]:
                if side in sides[other_num]:
                    matching_sides[num] += 1

    part1 = 1
    for num, count in matching_sides.items():
        if count == 4: # 4 matches because it will match each of its two sides twice: once for the original and once for the reverse
            part1 *= num

    return part1, 0
if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")