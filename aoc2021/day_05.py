from pathlib import Path

def solve():
    from collections import defaultdict
    lines = Path(__file__).with_name('day_05_input.txt').open('r').read().strip().split("\n")

    lines = [line.split(" -> ") for line in lines]
    lines = [[list(map(int, line[0].split(","))), list(map(int, line[1].split(",")))] for line in lines]

    part1Covered = defaultdict(int)
    part2Covered = defaultdict(int)

    for line in lines:

        if line[0][0] == line[1][0]:
            for i in range(min(line[0][1],line[1][1]), max(line[0][1],line[1][1])+1):
                part1Covered[(line[0][0], i)] += 1
                part2Covered[(line[0][0], i)] += 1
                
        elif line[0][1] == line[1][1]:
            for i in range(min(line[0][0],line[1][0]), max(line[0][0],line[1][0])+1):
                part1Covered[(i, line[0][1])] += 1
                part2Covered[(i, line[0][1])] += 1
        
        else:
            for i in range(abs(line[0][0]-line[1][0])+1):
                part2Covered[(line[0][0]+(i if line[0][0]<line[1][0] else -i), line[0][1]+(i if line[0][1]<line[1][1] else -i))] += 1

    part1 = 0
    part2 = 0
    for overlaps in part1Covered.values():
        if overlaps >= 2:
            part1 += 1
    for overlaps in part2Covered.values():
        if overlaps >= 2:
            part2 += 1
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")