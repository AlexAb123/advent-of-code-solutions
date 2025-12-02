from pathlib import Path

def solve():

    from collections import Counter
    lines = Path(__file__).with_name('day_02_input.txt').open('r').read().strip().split("\n")

    def get_all_combos_remove_one_char(str):
        combos = set()
        for i in range(len(str)):
            combos.add(str[0:i] + str[i+1:])
        return combos

    twos = 0
    threes = 0
    for i in range(len(lines)):
        counter = Counter(lines[i])
        two_counted = False
        three_counted = False
        for key in counter:
            if not two_counted and counter[key] == 2:
                twos += 1
                two_counted = True
            if not three_counted and counter[key] == 3:
                threes += 1
                three_counted = True
        for j in range(i+1, len(lines)):
            combos1 = get_all_combos_remove_one_char(lines[i])
            combos2 = get_all_combos_remove_one_char(lines[j])
            if len(combos1.intersection(combos2)) > 0:
                part2 = list(combos1.intersection(combos2))[0]
                break

    part1 = twos*threes

    return part1, part2


if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")