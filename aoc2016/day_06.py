from pathlib import Path

def solve():

    from collections import Counter

    lines = Path(__file__).with_name('day_06_input.txt').open('r').read().strip().split("\n")
    
    cols = [[line[i] for line in lines] for i in range(len(lines[0]))]
    part1 = ""
    part2 = ""
    for col in cols:
        counter = Counter(col)
        part1 += max(counter, key=counter.get)
        part2 += min(counter, key=counter.get)
        
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")

    print(f"Time Taken: {int((time() - start)*100000)/100} ms")