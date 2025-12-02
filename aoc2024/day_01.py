from pathlib import Path

def solve():
    
    from collections import Counter

    lines = [map(int, line.split()) for line in Path(__file__).with_name('day_01_input.txt').open('r').read().strip().split("\n")]
    left_list, right_list = map(sorted, zip(*lines))
    
    part1 = 0
    part2 = 0
    counter = Counter(right_list)
    
    for left, right in zip(left_list, right_list):
        part1 += abs(left - right)
        part2 += left * counter[left]
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")