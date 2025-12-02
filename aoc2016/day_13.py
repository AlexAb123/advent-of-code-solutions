from pathlib import Path

def solve():

    num = int(Path(__file__).with_name('day_13_input.txt').open('r').read().strip())

    def is_wall(x, y):
        return sum(b =="1" for b in bin((x*x + 3*x + 2*x*y + y + y*y) + num)[2:]) % 2 == 1

    start = 1 + 1j
    target = 31 + 39j
    q = [(start, 0)]
    seen = {start}
    part2 = 0
    while q:
        
        curr, dist = q.pop(0)

        if curr == target:
            part1 = dist

        if dist <= 50:
            part2 += 1

        for d in 1, -1, 1j, -1j:
            adj = curr + d
            if adj not in seen and not is_wall(int(adj.real), int(adj.imag)) and adj.real >= 0 and adj.imag >= 0:
                q.append((adj, dist + 1))
                seen.add(adj)

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")