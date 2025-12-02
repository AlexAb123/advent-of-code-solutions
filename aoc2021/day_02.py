from pathlib import Path

def solve():
    lines = Path(__file__).with_name('day_02_input.txt').open('r').read().strip().split("\n")

    lines = [line.split(" ") for line in lines]
    lines = [[line[0], int(line[1])] for line in lines]

    depth = 0
    x = 0
    for line in lines:
        if line[0] == "forward":
            x += line[1]
        elif line[0] == "down":
            depth += line[1]
        elif line[0] == "up":
            depth -= line[1]
    part1 = depth*x

    depth = 0
    x = 0
    aim = 0
    for line in lines:
        if line[0] == "forward":
            x += line[1]
            depth += aim * line[1]
        elif line[0] == "down":
            aim += line[1]
        elif line[0] == "up":
            aim -= line[1]
    part2 = depth*x
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")