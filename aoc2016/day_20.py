from pathlib import Path

def solve():

    ranges = [tuple(map(int, line.split("-"))) for line in Path(__file__).with_name('day_20_input.txt').open('r').read().strip().split("\n")]
    ranges = sorted([(r[0], r[1] + 1) for r in ranges])

    valid = 4294967295

    def overlap(r1, r2):
        return not (r1[0] > r2[1] or r1[1] < r2[0])
    def combine(r1, r2):
        return (min(r1[0], r2[0]), max(r1[1], r2[1]))
    
    i = len(ranges)-2
    while i > -1:
        if overlap(ranges[i], ranges[i+1]):
            ranges[i] = combine(ranges[i], ranges.pop(i+1))
            i = len(ranges)-2 # If we merged, go back to the start to make sure we don't miss any new merges that are possible after making this merge
            # Don't really know why you have to do this though, can't find a simple test case that doesn't work otherwise
        else:
            i -= 1
    disjoint_ranges = []
    for i in range(len(ranges)-1):
        disjoint_ranges.append((ranges[i][1], ranges[i+1][0]))
    disjoint_ranges.append((ranges[-1][1], valid + 1))
    part1 = disjoint_ranges[0][0]
    part2 = sum(r[1] - r[0] for r in disjoint_ranges)
    
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")