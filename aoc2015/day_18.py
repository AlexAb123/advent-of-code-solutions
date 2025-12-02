from pathlib import Path

def solve():

    lines = Path(__file__).with_name('day_18_input.txt').open('r').read().strip().split("\n")

    on1 = set()
    off1 = set()
    on2 = set()
    off2 = set()
    lights = set()
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            lights.add(r+c*1j)
            if lines[r][c] == "#":
                on1.add(r+c*1j)
                on2.add(r+c*1j)
            elif lines[r][c] == ".":
                off1.add(r+c*1j)
                off2.add(r+c*1j)
    off2.discard(0+0j)
    off2.discard(99)
    off2.discard(99j)
    off2.discard(99+99j)
    on2.add(0+0j)
    on2.add(99)
    on2.add(99j)
    on2.add(99+99j)

    def get_adjs(pos):
        for dr in -1,0,1:
            for dc in -1,0,1:
                if dr == dc == 0:
                    continue
                yield pos+dr+dc*1j

    def get_next_step(on, off):
        new_on, new_off = set(), set()
        for light in on | off:
            adjs_on = sum(adj in on for adj in get_adjs(light))
            if light in on:
                if adjs_on == 2 or adjs_on == 3:
                    new_on.add(light)
                else:
                    new_off.add(light)
            if light in off:
                if adjs_on == 3:
                    new_on.add(light)
                else:
                      new_off.add(light)
        return new_on, new_off


    for step in range(100):
        on1, off1 = get_next_step(on1, off1)
        on2, off2 = get_next_step(on2, off2)
        off2.discard(0+0j)
        off2.discard(99)
        off2.discard(99j)
        off2.discard(99+99j)
        on2.add(0+0j)
        on2.add(99)
        on2.add(99j)
        on2.add(99+99j)

    part1 = len(on1)
    part2 = len(on2)

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")