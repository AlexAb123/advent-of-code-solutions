from functools import cache

def solve(data):
    lines = data.split("\n")

    splits = set()
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == "S":
                start = (r, c)
            elif lines[r][c] == "^":
                splits.add((r, c))

    global part1
    part1 = 0
    @cache
    def timelines(r, c):
        if r >= len(lines):
            return 1
        if (r, c) in splits:
            global part1
            part1 += 1
            return timelines(r, c + 1) + timelines(r, c - 1)
        return timelines(r + 1, c)

    part2 = timelines(*start)

    return part1, part2


if __name__ == "__main__":
    from pathlib import Path
    from time import time
    data = (Path(__file__).parent / "inputs" / "day07.txt").read_text().strip()
    start = time()
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start) * 1000:.2f} ms")
