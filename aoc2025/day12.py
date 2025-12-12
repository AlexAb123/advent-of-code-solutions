def solve(data):

    lines = data.split("\n\n")
    regions = [line.split(": ") for line in lines[-1].split("\n")]
    regions = [[tuple(map(int, line[0].split("x"))), tuple(map(int, line[1].split(" ")))] for line in regions]
    part1 = sum(x * y >= sum(counts) * 9 for (x, y), counts in regions)
    part2 = "[Decorate the North Pole]"

    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    data = (Path(__file__).parent/"inputs"/"day12.txt").read_text().strip()
    start = time()
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")