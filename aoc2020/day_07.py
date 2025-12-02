from pathlib import Path
from collections import defaultdict
lines = Path(__file__).with_name('day_07_input.txt').open('r').read().strip().split("\n")
lines = [line.replace(" contain", ",").split(", ") for line in lines]
lines = [[rule.split(" ") for rule in line] for line in lines]

bags = defaultdict(list)
for line in lines:
    for rule in line[1:]:
        if rule[0] != "no":
            bags[line[0][0] + " " + line[0][1]].append([int(rule[0]), rule[1] + " " + rule[2]])

def hasShinyGold(bagName):
    hasGold = False
    if bagName not in bags:
        return False
    for bag in bags[bagName]:
        if bag[1] == 'shiny gold':
            return True
        hasGold = hasGold or hasShinyGold(bag[1])
    return hasGold

def totalBags(bagName):
    total = 0
    for bag in bags[bagName]:
        total += bag[0] + bag[0] * totalBags(bag[1]) 
    return total

totalGold = 0
for bag in bags.keys():
    totalGold += hasShinyGold(bag)

print(f"Part 1: {totalGold}")
print(f"Part 2: {totalBags('shiny gold')}")