from pathlib import Path

def solve():

    jumps1 = list(map(int, Path(__file__).with_name('day_05_input.txt').open('r').read().strip().split("\n")))
    jumps2 = jumps1.copy()

    i = 0
    steps = 0
    while 0 <= i and i < len(jumps1):
        jump = jumps1[i]
        jumps1[i] += 1
        i += jump
        steps += 1
    part1 = steps

    i = 0
    steps = 0
    while 0 <= i and i < len(jumps2):
        jump = jumps2[i]
        if jumps2[i] >= 3:
            jumps2[i] -= 1
        else:
            jumps2[i] += 1
        i += jump
        steps += 1

    part2 = steps
    
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")