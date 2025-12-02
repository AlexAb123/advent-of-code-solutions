from pathlib import Path

def solve():

    import re

    lines = [line.split("=") for line in Path(__file__).with_name('day_23_input.txt').open('r').read().strip().split("\n")]
    nanobots = set((*map(int, re.findall(r"<(.*?)>", line[1])[0].split(",")), int(line[-1])) for line in lines)
    max_bot = max(nanobots, key = lambda bot: bot[3])
    part1 = sum(abs(max_bot[0] - bot[0]) + abs(max_bot[1] - bot[1]) + abs(max_bot[2] - bot[2]) <= max_bot[3] for bot in nanobots)


    part2 = 0

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")