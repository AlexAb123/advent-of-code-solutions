def solve(data):

    fresh, available = list(map(lambda x: x.split("\n"), data.split("\n\n")))
    fresh = sorted([tuple(map(int, f.split("-"))) for f in fresh])
    available = list(map(int, available))

    combined = [fresh[0]]
    for l2, r2 in fresh[1:]:
        l1, r1 = combined[-1]
        if r1 >= l2:
            # Only need to check overlapping in one direction. 
            # The other direction will get checked on the next iteration.
            combined[-1] = (l1, max(r1, r2)) # Combine ranges.
        else:
            combined.append((l2, r2)) # Ranges don't overlap, append.
            
    part1 = part2 = 0
    for l, r in combined:
        for num in available:
            if l <= num <= r:
                part1 += 1
        part2 += r - l + 1

    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    start = time()
    part1, part2 = solve((Path(__file__).parent/"inputs"/"day05.txt").read_text().strip())
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")