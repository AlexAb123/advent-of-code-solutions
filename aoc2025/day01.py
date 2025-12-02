def solve(input_path):

    lines = input_path.open('r').read().strip().split("\n")

    part1 = 0
    part2 = 0

    dial = 50
    for line in lines:
        move = int(line[1:])
        sign, dist_to_zero = (-1, dial) if line[0] == "L" else (1, 100 - dial)
        
        part2 += move // 100
        part2 += move > dist_to_zero
        
        dial = (dial + sign * move) % 100
        
        part1 += dial == 0

    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    start = time()
    part1, part2 = solve(Path(__file__).parent/"inputs"/"day01.txt")
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")