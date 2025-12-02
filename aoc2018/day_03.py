from pathlib import Path

def solve():

    from collections import defaultdict
    lines = [line.replace(" @", "").replace("#", "").replace(":", "").replace("x", ",").split(" ") for line in Path(__file__).with_name('day_03_input.txt').open('r').read().strip().split("\n")]

    def box_overlap(pos1, size1, pos2, size2):
        claims = set()
        for x in range(1, size1[0]+1):
            for y in range(1, size1[1]+1):
                claims.add((pos1[0]+x, pos1[1]+y))

        for x in range(1, size2[0]+1):
            for y in range(1, size2[1]+1):
                if (pos2[0]+x, pos2[1]+y) in claims:
                    return True
        return False

    claims = defaultdict(int)
    for line in lines:
        claim_id = int(line[0])
        pos = tuple(map(int, line[1].split(",")))
        size = tuple(map(int, line[2].split(",")))

        for x in range(1, size[0]+1):
            for y in range(1, size[1]+1):
                claims[(pos[0]+x, pos[1]+y)] += 1

    part1 = 0
    for key in claims:
        if claims[key] > 1:
            part1 += 1

    for i in range(len(lines)):
        overlap = False
        claim_id = int(lines[i][0])
        for j in range(len(lines)):
            if i == j:
                continue
            pos1 = tuple(map(int, lines[i][1].split(",")))
            size1 = tuple(map(int, lines[i][2].split(",")))
            pos2 = tuple(map(int, lines[j][1].split(",")))
            size2 = tuple(map(int, lines[j][2].split(",")))
            if box_overlap(pos1, size1, pos2, size2):
                overlap = True
                break
        if not overlap:
            part2 = claim_id
            break

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")