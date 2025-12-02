from pathlib import Path

def solve():

    import re

    lines = Path(__file__).with_name('day_15_input.txt').open('r').read().strip().split("\n")

    discs = []
    for line in lines:
        _, num_pos, _, pos = map(int, re.findall(r'\d+', line))
        discs.append((num_pos, pos))
    
    def get_capsule(discs, t):
        for i in range(len(discs)):
            disc, num_pos, pos = i + 1, *discs[i]
            if (t + disc + pos) % num_pos != 0:
                return False
        return True

    def get_time(discs):
        t = 0
        while True:
            if get_capsule(discs, t):
                break
            t += 1
        return t
    
    part1 = get_time(discs)
    discs.append((11, 0))
    part2 = get_time(discs)
   
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")