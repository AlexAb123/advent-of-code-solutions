from pathlib import Path

def solve():

    lines = Path(__file__).with_name('day_17_input.txt').open('r').read().strip().split("\n")

    print(lines)

    part1 = 0
    part2 = 0

    

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")