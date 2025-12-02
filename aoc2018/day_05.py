from pathlib import Path

def solve():

    polymer = list(Path(__file__).with_name('day_05_input.txt').open('r').read().strip())

    def is_reactive(s1, s2):
        return (s1 == s1.lower() and s2 == s2.upper() and s1.lower() == s2.lower()) or (s2 == s2.lower() and s1 == s1.upper() and s2.lower() == s1.lower())

    def react_polymer(polymer, types):
        reactions = None
        while reactions != 0:
            reactions = 0
            new_polymer = []
            i = 0
            while i < len(polymer) - 1:
                if polymer[i].lower() in types and is_reactive(polymer[i], polymer[i+1]):
                    reactions += 1
                    i += 2
                else:
                    new_polymer.append(polymer[i])
                    i += 1
                if i == len(polymer) - 1:
                    new_polymer.append(polymer[i])
            polymer = new_polymer.copy()
        return polymer

    types = "abcdefghijklmnopqrstuvwxyz"
    part1 = len(react_polymer(polymer.copy(), types))
    shortest_length = float('inf')
    for possible_type in types:
        shortest_length = min(shortest_length, len(react_polymer(list(filter(lambda x: x.lower() != possible_type, polymer.copy())), types)))
    part2 = shortest_length

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")