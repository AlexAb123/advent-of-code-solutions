def solve(data):

    lines = data.split("\n")

    part1 = 0
    part2 = 0

    

    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    start = time()
    part1, part2 = solve((Path(__file__).parent/"inputs"/"day09.txt").read_text().strip())
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")