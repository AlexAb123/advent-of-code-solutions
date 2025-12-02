from pathlib import Path
def solve():

    lines1 = [list(map(int, filter(lambda x: x != "", line.split(" ")))) for line in Path(__file__).with_name('day_03_input.txt').open('r').read().strip().split("\n")]
    lines2 = [sorted([lines1[r][c], lines1[r+1][c], lines1[r+2][c]]) for r in range(0, len(lines1)-2, 3) for c in range(3)]
    lines1 = map(sorted, lines1)

    part1 = sum(map(lambda x: int(x[0] + x[1] > x[2]), lines1))
    part2 = sum(map(lambda x: int(x[0] + x[1] > x[2]), lines2))
    
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")