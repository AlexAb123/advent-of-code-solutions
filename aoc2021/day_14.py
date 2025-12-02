from pathlib import Path

def solve():

    from collections import defaultdict

    polymer, rules = Path(__file__).with_name('day_14_input.txt').open('r').read().strip().split("\n\n")
    rules = {rule.split(" -> ")[0]: rule.split(" -> ")[1] for rule in rules.split("\n")}

    cache = {}
    def step_polymer(polymer, steps_left):
        
        if (polymer, steps_left) in cache:
            return cache[(polymer, steps_left)]
        
        counts = defaultdict(int)
        
        if steps_left == 0:
            return counts
        
        new_polymer = polymer[0] + rules[polymer] + polymer[1]
        counts[rules[polymer]] += 1

        for element, count in step_polymer(new_polymer[:2], steps_left-1).items():
            counts[element] += count

        for element, count in step_polymer(new_polymer[1:], steps_left-1).items():
            counts[element] += count

        cache[(polymer, steps_left)] = counts
        return counts

    counter_part2 = defaultdict(int)
    counter_part1 = defaultdict(int)

    for element in polymer:
        counter_part1[element] += 1
        counter_part2[element] += 1

    for i in range(len(polymer)-1):
        for element, count in step_polymer(polymer[i:i+2], 10).items():
            counter_part1[element] += count
        for element, count in step_polymer(polymer[i:i+2], 40).items():
            counter_part2[element] += count

    part1 = max(counter_part1.values()) - min(counter_part1.values())
    part2 = max(counter_part2.values()) - min(counter_part2.values())

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")