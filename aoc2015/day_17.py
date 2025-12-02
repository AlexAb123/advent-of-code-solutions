from pathlib import Path

def solve():

    containers = tuple(map(int, Path(__file__).with_name('day_17_input.txt').open('r').read().strip().split("\n")))

    liters_needed = 150

    seen = set()
    def get_combos(containers_left, capacity):
        if containers_left in seen:
            return set()
        seen.add(containers_left)
        if capacity > liters_needed:
            return set()
        elif capacity == liters_needed:
            return {containers_left}

        combos = set()
        for i, container in enumerate(containers_left):
            if container == -1:
                continue
            combos.update(get_combos(containers_left[:i] + (-1, ) + containers_left[i+1:], capacity + container))
        return combos

    combos = get_combos(containers, 0)

    part1 = len(combos)

    min_containers = min(combos, key=lambda x: x.count(-1)).count(-1)
    part2 = len(list(filter(lambda x: x.count(-1) == min_containers, combos)))

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")