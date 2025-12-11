from pathlib import Path

def solve():

    lines = [tuple(map(int, line.split(","))) for line in Path(__file__).with_name('day_25_input.txt').open('r').read().strip().split("\n")]

    part1 = 0
    part2 = 0
    
    def d(p1, p2):
        x1, y1, z1, w1 = p1
        x2, y2, z2, w2 = p2
        return abs(x1-x2) + abs(y1-y2) + abs(z1-z2) + abs(w1-w2)
    
    def adjs(curr):
        for adj in lines:
            if d(curr, adj) <= 3:
                yield adj
    seen = set()
    for line in lines:
        if line in seen:
            continue
        part1 += 1
        q = [line]
        seen.add(line)
        while q:
            curr = q.pop(0)
            for adj in adjs(curr):
                if adj in seen:
                    continue
                q.append(adj)
                seen.add(adj)
                
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")