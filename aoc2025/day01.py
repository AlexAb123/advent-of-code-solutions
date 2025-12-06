def solve(data):

    lines = data.split("\n")

    part1 = part2 = 0

    dial = 50
    for line in lines:
        move = int(line[1:])
        sign = -1 if line[0] == "L" else 1
        dist_to_zero = dial if line[0] == "L" or dial == 0 else 100 - dial

        part2 += move // 100
        part2 += (move % 100) > dist_to_zero

        dial = (dial + sign * move) % 100

        part1 += dial == 0

    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    data = (Path(__file__).parent/"inputs"/"day01.txt").read_text().strip()
    start = time()
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")