from pathlib import Path

def solve():

    lines = [list(map(int, line.split("\t"))) for line in Path(__file__).with_name('day_02_input.txt').open('r').read().strip().split("\n")]

    part1 = sum(map(lambda line: max(line) - min(line), lines))

    part2 = 0
    for line in lines:
        found = False
        for i in range(len(line)):
            for j in range(i+1, len(line)):
                if line[i] % line[j] == 0:
                    part2 += line[i]//line[j]
                    found = True
                    break
                elif line[j] % line[i] == 0:
                    part2 += line[j]//line[i]
                    found = True
                    break
            if found:
                break
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")