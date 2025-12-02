from pathlib import Path

def solve():
    
    lines = Path(__file__).with_name('day_12_input.txt').open('r').read().strip().split("\n")
    grid = {r+c*1j: lines[r][c] for c in range(len(lines[0])) for r in range(len(lines))}

    def find_region(pos, grid):
        region = {pos}
        visited.add(pos)
        for adj in pos+1, pos-1, pos+1j, pos-1j:
            if adj in grid and adj not in visited and grid[pos] == grid[adj]:
                region |= find_region(adj, grid)
        return region

    def region_perimeter(region):
        # Perimeter is stored as a set of tuples
        # Each tuple is (pos, dir) where pos is in the region but pos+dir isnt
        # A single position could have multiple occurences in the perimeter, like a corner
        perimeter = set()
        for pos in region:
            for adj in pos+1, pos-1, pos+1j, pos-1j:
                if adj not in region:
                    perimeter.add((pos, adj-pos))
        return perimeter

    def region_sides(perimeter):
        # If the thing to our left (could choose right, just have to choose one)
        # is not in the perimeter with the same direction, then we are at a corner/we made a turn
        # # of corners = # of turns = # of sides
        return len(perimeter - {(pos+d*1j, d) for pos, d in perimeter})
    
    visited = set()
    regions = []
    for pos in grid:
        if pos in visited:
            continue
        region = find_region(pos, grid)
        perimeter = region_perimeter(region)
        regions.append((len(region), len(perimeter), region_sides(perimeter)))

    part1 = sum(region[0] * region[1] for region in regions)
    part2 = sum(region[0] * region[2] for region in regions)

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")