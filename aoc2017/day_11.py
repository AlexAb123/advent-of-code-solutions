from pathlib import Path

def solve():

    lines = Path(__file__).with_name('day_11_input.txt').open('r').read().strip().split(",")

    print(lines)

    part1 = 0
    part2 = 0

    ds = {"n": -1, 
          "ne": -0.5 + 0.5j,
          "se": 0.5 + 0.5j,
          "s" : 1,
          "sw": 0.5 - 0.5j,
          "nw": -0.5 - 0.5j}
    
    # ne,se breaks it. should be 2 but this gives 1

    pos = 0+0j
    for d in lines:
        pos += ds[d]

    part1 = int(abs(pos.real) + abs(pos.imag))
    return part1, part2

# 338 too low

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")