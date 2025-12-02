from pathlib import Path

def solve():
    
    schematics = [int(schematic.replace("\n", ""), 2) for schematic in  Path(__file__).with_name('day_25_input.txt').open('r').read().strip().replace("#", "1").replace(".", "0").split("\n\n")]
    locks = set()
    keys = set()
    for schematic in schematics:
        if schematic & 1 == 0:
            locks.add(schematic)
        else:
            keys.add(schematic)
    part1 = sum(1 for lock in locks for key in keys if lock & key == 0)
    part2 = "[Deliver The Chronicle]"
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")