from pathlib import Path

def solve():

    lines = Path(__file__).with_name('day_17_input.txt').open('r').read().strip().split("\n")

    active_cubes1 = set()
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == "#":
                active_cubes1.add((c, r, 0))

    active_cubes2 = set()
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == "#":
                active_cubes2.add((c, r, 0, 0))

    cycles = 6
    min_x = min(active_cubes2, key=lambda p: p[0])[0] - cycles
    max_x = max(active_cubes2, key=lambda p: p[0])[0] + cycles
    min_y = min(active_cubes2, key=lambda p: p[1])[1] - cycles
    max_y = max(active_cubes2, key=lambda p: p[1])[1] + cycles
    min_z = -cycles
    max_z = cycles
    min_w = -cycles
    max_w = cycles

    inactive_cubes1 = set()
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            for z in range(min_z, max_z+1):
                if (x, y, z) not in active_cubes2:
                    inactive_cubes1.add((x, y, z))

    inactive_cubes2 = set()
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            for z in range(min_z, max_z+1):
                for w in range(min_w, max_w+1):
                    if (x, y, z, w) not in active_cubes2:
                        inactive_cubes2.add((x, y, z, w))

    def get_adjs_3d(x, y, z):
        for dx in -1,0,1:
            for dy in -1,0,1:
                for dz in -1,0,1:
                    if dx == dy == dz == 0:
                        continue
                    yield (x+dx, y+dy, z+dz)

    def get_adjs_4d(x, y, z, w):
        for dx in -1,0,1:
            for dy in -1,0,1:
                for dz in -1,0,1:
                    for dw in -1,0,1:
                        if dx == dy == dz == dw == 0:
                            continue
                        yield (x+dx, y+dy, z+dz, w+dw)

    def get_active_adjs(pos, active_cubes, part2):
        active_adjs = 0
        adjs = get_adjs_3d(*pos) if not part2 else get_adjs_4d(*pos)
        for adj in adjs:
            if adj in active_cubes:
                active_adjs += 1
        return active_adjs

    def simulate_cycles(active_cubes, inactive_cubes, cycles_left, part2):
        if cycles_left == 0:
            return active_cubes, inactive_cubes
        
        new_active_cubes = set()
        new_inactive_cubes = set()

        for cube in active_cubes:
            active_adjs = get_active_adjs(cube, active_cubes, part2)
            if active_adjs == 2 or active_adjs == 3:
                new_active_cubes.add(cube)
            else:
                new_inactive_cubes.add(cube)

        for cube in inactive_cubes:
            active_adjs = get_active_adjs(cube, active_cubes, part2)
            if active_adjs == 3:
                new_active_cubes.add(cube)
            else:
                new_inactive_cubes.add(cube)

        return simulate_cycles(new_active_cubes, new_inactive_cubes, cycles_left-1, part2)

    active_cubes1, inactive_cubes1 = simulate_cycles(active_cubes1, inactive_cubes1, 6, False)
    active_cubes2, inactive_cubes2 = simulate_cycles(active_cubes2, inactive_cubes2, 6, True)
    part1 = len(active_cubes1)
    part2 = len(active_cubes2)

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")