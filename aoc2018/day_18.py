from pathlib import Path

def solve():

    lines = Path(__file__).with_name('day_18_input.txt').open('r').read().strip().split("\n")

    rows = len(lines)
    cols = len(lines[0])

    empty = set()
    trees = set()
    lumberyard = set()
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == ".":
                empty.add(r + c * 1j)
            elif lines[r][c] == "|":
                trees.add(r + c * 1j)
            elif lines[r][c] == "#":
                lumberyard.add(r + c * 1j)


    def adjacent_types(r, c, empty, trees, lumberyard):
        for dr in -1, 0, 1:
            for dc in -1, 0, 1:
                if dr == dc == 0:
                    continue


    def update(empty, trees, lumberyard):
        
        new_empty = empty.copy()
        new_trees = trees.copy()
        new_lumberyard = lumberyard.copy()

        for r in range(rows):
            for c in range(cols):

                empty_count = 0
                tree_count = 0
                lumberyard_count = 0
                for dr in -1, 0, 1:
                    for dc in -1, 0, 1:
                        if dr == dc == 0:
                            continue
                        adj = (r + dr) + (c + dc) * 1j
                        if adj in empty:
                            empty_count += 1
                        elif adj in trees:
                            tree_count += 1
                        elif adj in lumberyard:
                            lumberyard_count += 1
                pos = (r + c * 1j)

                if pos in empty and tree_count >= 3:
                    new_empty.remove(pos)
                    new_trees.add(pos)

                if pos in trees and lumberyard_count >= 3:
                    new_lumberyard.add(pos)
                    new_trees.remove(pos)

                if pos in lumberyard and not (lumberyard_count >= 1 and tree_count >= 1):
                    new_lumberyard.remove(pos)
                    new_empty.add(pos)

        return new_empty, new_trees, new_lumberyard
    
    def visualize(empty, trees, lumberyard):
        grid = [["." for _ in range(cols)] for _ in range(rows)]
        for pos in empty:
            grid[int(pos.real)][int(pos.imag)] = "."
        for pos in trees:
            grid[int(pos.real)][int(pos.imag)] = "|"
        for pos in lumberyard:
            grid[int(pos.real)][int(pos.imag)] = "#"
        string = ""
        for line in grid:
            string += "".join(line) + "\n"
        return string
    
    states = []
    for minute in range(1000000000):
        if minute == 10:
            part1 = len(trees) * len(lumberyard)
        if (frozenset(empty), frozenset(trees), frozenset(lumberyard)) in states:
            cycle_start = states.index((frozenset(empty), frozenset(trees), frozenset(lumberyard)))
            break
        states.append((frozenset(empty), frozenset(trees), frozenset(lumberyard)))
        empty, trees, lumberyard = update(empty, trees, lumberyard)
        
    cycle_length =  len(states) - cycle_start
    part2 = 0
    final_state = states[((1000000000 - cycle_start) % cycle_length) + cycle_start]
    part2 = len(final_state[1]) * len(final_state[2])

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")