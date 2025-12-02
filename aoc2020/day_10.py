from pathlib import Path
from collections import defaultdict
lines = sorted(list(map(int, Path(__file__).with_name('day_10_input.txt').open('r').read().strip().split("\n"))))

differences = []
joltage = 0
for line in lines:
    differences.append(line-joltage)
    joltage = line
differences.append(3)

def part1(differences):
    ones = 0
    threes = 0
    for n in differences:
        if n == 1:
            ones += 1
        if n == 3:
            threes += 1
    return ones*threes
print(f"Part 1: {part1(differences)}")

cache = {}
def isValidArrangement(current):

    if current in cache:
        return cache[current]

    if current+1 in lines or current+2 in lines or current+3 in lines:
        ret = 0
        if current+1 in lines:
            ret += isValidArrangement(current+1)
        if current+2 in lines:
            ret += isValidArrangement(current+2)
        if current+3 in lines:
            ret += isValidArrangement(current+3)
        cache[current] = ret
        return ret

    elif current == lines[-1]:
        return 1
    else:
        return 0

print(f"Part 2: {isValidArrangement(0)}")