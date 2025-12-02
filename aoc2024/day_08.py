from pathlib import Path


def solve():
    from collections import defaultdict

    def in_bounds(pos):
        return 0 <= pos[0] < len(lines) and 0 <= pos[1] < len(lines[0])
        
    lines = Path(__file__).with_name('day_08_input.txt').open('r').read().strip().split("\n")
    frequencies = defaultdict(list)
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] != ".":
                frequencies[lines[r][c]].append((r,c))

    antinodes_part1 = set()
    antinodes_part2 = set()
    
    for antennas in frequencies.values():

        for antenna1 in antennas:
            for antenna2 in antennas:
                
                if antenna1 == antenna2:
                    continue

                dr, dc = antenna1[0] - antenna2[0], antenna1[1] - antenna2[1]
                if in_bounds(a := (antenna1[0] + dr, antenna1[1] + dc)):
                    antinodes_part1.add(a)

                next_antinode = antenna1
                while in_bounds(next_antinode):
                    antinodes_part2.add(next_antinode)
                    next_antinode = (next_antinode[0] + dr, next_antinode[1] + dc)

    return len(antinodes_part1), len(antinodes_part2)

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")