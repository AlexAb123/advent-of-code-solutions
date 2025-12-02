from pathlib import Path

def solve():
    lines = list(map(int, Path(__file__).with_name('day_01_input.txt').open('r').read().strip().split("\n")))
    part1 = sum(lines[i] < lines[i+1] for i in range(len(lines)-1))
    part2 = sum(lines[i] < lines[i+3] for i in range(len(lines)-3))
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")