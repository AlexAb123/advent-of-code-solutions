from pathlib import Path

def solve():
    
    from collections import defaultdict

    lines = Path(__file__).with_name('day_16_input.txt').open('r').read().strip().split("\n")

    sues = defaultdict(dict)
    for line in lines:
        line = line.split(" ")
        sues[int(line[1][:-1])][line[2][:-1]] = int(line[3][:-1])
        sues[int(line[1][:-1])][line[4][:-1]] = int(line[5][:-1])
        sues[int(line[1][:-1])][line[6][:-1]] = int(line[7])

    props = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }
    greater = {"cats", "trees"}
    less = {"pomeranians", "goldfish"}

    def is_real_sue(sue, part2):
        for prop in sue:

            if part2:

                if prop in greater:
                    if sue[prop] <= props[prop]:
                        return False
                elif prop in less:
                    if sue[prop] >= props[prop]:
                        return False
                else:
                    if sue[prop] != props[prop]:
                        return False

            elif sue[prop] != props[prop]:
                return False
        return True

    for num, sue in sues.items():
        if is_real_sue(sue, False):
            part1 = num
        elif is_real_sue(sue, True):
            part2 = num

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")