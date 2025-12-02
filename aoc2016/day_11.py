from pathlib import Path

def solve():

    import re
    import math
    from heapq import heappush, heappop
    from collections import defaultdict

    lines = Path(__file__).with_name('day_11_input.txt').open('r').read().strip().split("\n")

    lines[0] = lines[0] + "An elerium generator. An elerium-compatible microchip. A dilithium generator. A dilithium-compatible microchip."

    def is_valid_state(floors):
        for floor in floors:
            for chip in floor[1]:
                if len(floor[0]) > 0 and chip not in floor[0]: # If this chip is not powered by its own RTG and there is another RTG on this floor
                    return False
        return True
    
    def heuristic(floors):
        total = 0
        for i in range(len(floors)):
            total += math.ceil((len(floors[i][0]) + len(floors[i][1])) / 2.0) * (len(floors) - i)
        return total

    all_items = (frozenset(), frozenset())
    floors = () # Each floor is (frozenset of generators, frozenset of chips)
    for line in lines:
        generators = frozenset(re.findall(r"(\w+) generator", line))
        chips = frozenset(re.findall(r"(\w+)-compatible microchip", line))
        all_items = (all_items[0].union(generators), all_items[1].union(chips))
        floor = (generators, chips)
        floors += (floor,)
    target = tuple((frozenset(), frozenset()) for i in range(len(floors) - 1))
    target += (all_items,)
    target = (target, len(floors) - 1)

    def get_combos(generators, chips):
        generators = list(generators)
        chips = list(chips)

        for generator in generators:
            yield (frozenset({generator}), frozenset())
        for chip in chips:
            yield (frozenset(), frozenset({chip}))
        
        for generator in generators:
            for chip in chips:
                yield (frozenset({generator}), frozenset({chip}))

        for i in range(len(generators)):
            for j in range(i+1, len(generators)):
                yield (frozenset({generators[i], generators[j]}), frozenset())
        for i in range(len(chips)):
            for j in range(i+1, len(chips)):
                yield (frozenset(), frozenset({chips[i], chips[j]}))

    def get_adjs(floors, curr_floor):
        for combo in get_combos(*floors[curr_floor]):
            generators, chips = combo

            for target_floor in range(len(floors)):
                if abs(curr_floor - target_floor) != 1 or target_floor == curr_floor:
                    continue

                new_floors = tuple()
                for i in range(len(floors)):

                    if i == curr_floor: # Remove the items from current floor
                        new_floors += ((floors[i][0].difference(generators), floors[i][1].difference(chips)),)
                    elif i == target_floor: # Add the items to target floor
                        new_floors += ((floors[i][0].union(generators), floors[i][1].union(chips)),)
                    else: # Keep other floors the same
                        new_floors += (floors[i],)

                yield new_floors, target_floor

    start = (floors, 0)
    q = [(heuristic(floors), start)]
    visited = {start}
    dists = defaultdict(lambda: float('inf'))
    dists[start] = 0
    while q:

        _, curr = heappop(q)
        visited.add(curr)
        if curr == target:
            part1 = dists[curr]
            break

        for adj in get_adjs(*curr):

            if adj in visited:
                continue
            if not is_valid_state(adj[0]):
                continue

            h = heuristic(adj[0])
            f = dists[curr] + h

            if dists[curr] + 1 >= dists[adj]:
                continue

            if dists[curr] + 1 < dists[adj]:
                dists[adj] = dists[curr] + 1

            heappush(q, (dists[curr] + 1 + h, adj))

    part2 = 0
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")