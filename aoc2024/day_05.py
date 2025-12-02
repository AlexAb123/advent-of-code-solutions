from pathlib import Path

def solve():
    from collections import defaultdict

    lines = Path(__file__).with_name('day_05_input.txt').open('r').read().strip().split("\n")

    rules = defaultdict(set)
    updates = []

    for line in lines:
        if "|" in line:
            rules[int(line.split("|")[0])].add(int(line.split("|")[1]))
        elif line != "":
            updates.append(list(map(int, line.split(","))))

    def is_safe(update):
        seen = set()
        for num in update:
            for after in rules[num]:
                if after in seen:
                    return False
            seen.add(num)
        return True

    def make_safe(update):
        sort_key = defaultdict(int)
        for num in update:
            for after in rules[num]:
                if after in update:
                    sort_key[num] += 1
        return sorted(update, key=lambda num: sort_key[num], reverse=True)
    
    part1 = 0
    part2 = 0
    for update in updates:
        if is_safe(update):
            part1 += update[len(update)//2]
        else:
            part2 += make_safe(update)[len(update)//2]

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")