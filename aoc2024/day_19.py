from pathlib import Path

def solve():
        
    patterns, designs = Path(__file__).with_name('day_19_input.txt').open('r').read().strip().split("\n\n")
    patterns = set(patterns.split(", "))
    designs = set(designs.split("\n"))

    pattern_max_length = max(map(lambda x: len(x), patterns))

    cache = {}
    def ways_to_make_design(design):
        if design in cache:
            return cache[design]
        if len(design) == 0:
            return 1
        ways = 0
        for i in range(min(pattern_max_length, len(design))):
            if design[:i+1] in patterns:
                ways += ways_to_make_design(design[i+1:])
        cache[design] = ways
        return ways

    part1 = 0
    part2 = 0
    for design in designs:
        ways = ways_to_make_design(design)
        if ways:
            part1 += 1
            part2 += ways
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")