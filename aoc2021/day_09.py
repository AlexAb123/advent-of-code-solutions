from pathlib import Path

def solve():
    lines = Path(__file__).with_name('day_09_input.txt').open('r').read().strip().split("\n")

    grid = {r+c*1j: int(lines[r][c]) for c in range(len(lines[0])) for r in range(len(lines))}

    low_points = set()
    part1 = 0
    for pos in grid:
        if all(grid[adj] > grid[pos] for adj in (pos+1, pos-1, pos+1j, pos-1j) if adj in grid):
            part1 += grid[pos] + 1
            low_points.add(pos)
    
    def find_basin(pos, visited):
        visited.add(pos)
        for adj in pos+1, pos-1, pos+1j, pos-1j:
            if adj not in grid:
                continue
            if adj not in visited and grid[adj] != 9 and grid[adj] > grid[pos]:
                find_basin(adj, visited)
        return visited

    basins = []
    for low_point in low_points:
        basins.append(len(find_basin(low_point, set())))
    part2 = 1
    for basin in sorted(basins, reverse=True)[0:3]:
        part2 *= basin
        
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")