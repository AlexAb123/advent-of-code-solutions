from pathlib import Path

def solve():

    from collections import defaultdict
    from functools import lru_cache

    replacement_strings, molecule = Path(__file__).with_name('day_19_input.txt').open('r').read().strip().split("\n\n")
    molecule = tuple(molecule)
    replacements = defaultdict(set)
    reverse_replacements = defaultdict(set)
    for replacement in replacement_strings.split("\n"):
        char, replacement = replacement.split(" => ")
        replacements[tuple(char)].add(tuple(replacement))
        reverse_replacements[tuple(replacement)].add(tuple(char))

    print(replacements)

    @lru_cache
    def get_next_possibilites(molecule):
        possibilities = set()
        for char, replacement_set in replacements.items():
            for i in range(len(molecule)+1-len(char)):
                if molecule[i:i+len(char)] != char:
                    continue
                for replacement in replacement_set:
                    possibilities.add(molecule[:i] + replacement + molecule[i+len(char):])
        return possibilities
    
    @lru_cache
    def get_next_possibilites_reverse(molecule):
        possibilities = set()
        for char, replacement_set in reverse_replacements.items():
            for replacement in replacement_set:
                for i in range(len(molecule)+1-len(char)):
                    if molecule[i:i+len(char)] != char:
                        continue
                    possibilities.add(molecule[:i] + replacement + molecule[i+len(char):])
        return possibilities
    
    part1 = len(get_next_possibilites(molecule))
    
    possibilities = {molecule}
    steps = 0
    seen = set()
    while ("e",) not in possibilities:
        new_possibilities = set()
        for possibility in possibilities:
            if possibility in seen:
                continue
            print(len(possibilities))
            print(len(possibility))
            new_possibilities.update(get_next_possibilites_reverse(possibility))
            seen.add(possibility)
        possibilities = new_possibilities
        steps += 1
        print(steps)
    part2 = steps
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")

# 505 too high p2