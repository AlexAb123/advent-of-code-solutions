from pathlib import Path

def solve():

    from collections import defaultdict

    lines = Path(__file__).with_name('day_13_input.txt').open('r').read().strip().split("\n")

    adjs = defaultdict(dict)
    people = set()
    for line in lines:
        source = line.split(" ")[0]
        num = int(line.split(" ")[3])
        target = line.split(" ")[-1][:-1]
        if "gain" in line:
            sign = 1
        else:
            sign = -1
        adjs[source][target] = sign*num
        people.add(source)

    def get_arrangements(curr, order):
        order += (curr,)
        if len(order) == len(people):
            return {order}
        arrangements = set()
        for person in people:
            if person in order:
                continue
            arrangements.update(get_arrangements(person, order))
        return arrangements
    
    def get_happiness(arrangement, adjs):
        happiness = 0
        for i, curr in enumerate(arrangement):
            happiness += adjs[curr][arrangement[(i+1)%len(arrangement)]]
            happiness += adjs[curr][arrangement[(i-1)%len(arrangement)]]
        return happiness
    
    arrangements = set()
    for person in people:
        arrangements.update(get_arrangements(person, tuple()))

    max_happiness = float("-inf")
    for arrangement in arrangements:
        max_happiness = max(max_happiness, get_happiness(arrangement, adjs))
    part1 = max_happiness

    for v in adjs.values():
        v["You"] = 0
    for person in people:
        adjs["You"][person] = 0
    people.add("You")

    arrangements = set()
    for person in people:
        arrangements.update(get_arrangements(person, tuple()))

    max_happiness = float("-inf")
    for arrangement in arrangements:
        max_happiness = max(max_happiness, get_happiness(arrangement, adjs))
    part2 = max_happiness

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")
