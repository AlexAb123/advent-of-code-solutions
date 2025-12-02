from pathlib import Path

def solve():

    from math import log

    num = int(Path(__file__).with_name('day_19_input.txt').open('r').read().strip())

    part1 = ((num - (2 ** int(log(num, 2)))) * 2) + 1
    part2 = num - (3 ** int(log(num, 3)))
    if part2 > 3 ** int(log(num, 3)):
        part2 += num - (2 * (3 ** int(log(num, 3))))
        
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")