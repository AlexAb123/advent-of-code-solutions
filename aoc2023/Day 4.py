import sys
sys.path.append("Python")
from Library import *
from collections import defaultdict

file = open('Python/Advent_of_Code/AOC2023/day 4 input.txt', 'r')
input = file.read().strip().split("\n")

input = [input[i].split(":") for i in range(len(input))]
for i in range(len(input)):
    input[i][1] = input[i][1].split("|")
for i in range(len(input)):
    input[i][1][0] = input[i][1][0].split(" ")
    input[i][1][1] = input[i][1][1].split(" ")

matches = defaultdict(list)

score1 = 0

for card in range(len(input)):
    have = set(h for h in input[card][1][1] if h.isdigit())
    win = set(h for h in input[card][1][0] if h.isdigit())
    matches[card] = len(have.intersection(win))
    score1 += int(2**(matches[card]-1))

score2 = 0

numCards = [1 for i in range(len(input))]

for card, num in enumerate(numCards):
    for i in range(matches[card]):
        numCards[card+i+1] = numCards[card+i+1] + num
        score2 += num

print(f"Part 1: {score1}")
print(f"Part 2: {score2}")