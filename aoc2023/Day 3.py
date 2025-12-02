import sys
sys.path.append("Python")
from Library import *
import collections

file = open('Python/Advent_of_Code/AOC2023/day 3 input.txt', 'r')
input = file.read().strip().split("\n")

input = [[c for c in r] for r in input]

starDict = collections.defaultdict(list)
part1Score = 0
rows = len(input)
cols = len(input[0])
for row in range(len(input)):
    starsInRow = set()
    currentNum = ""
    adjacentSymbol = False
    for col in range(len(input[row])+1):
        if col < len(input[0]) and input[row][col].isdigit():
            currentNum += input[row][col]

            for r in [-1,0,1]:
                for c in [-1,0,1]:
                    if 0 <= row+r < rows and 0 <= col+c < cols:
                        if not input[row+r][col+c].isdigit() and input[row+r][col+c] != ".":
                            adjacentSymbol = True
                        if input[row+r][col+c] == "*":
                            starsInRow.add((row+r,col+c))
        elif currentNum.isdigit():
            for star in starsInRow:
                starDict[star].append(int(currentNum))
                starsInRow = set()
            if adjacentSymbol:
                part1Score += int(currentNum)
                adjacentSymbol = False
            currentNum = ""

part2Score = 0
for key, val in starDict.items():
    if len(val) == 2:
        part2Score += val[0] * val[1]

print(f"Part 1: {part1Score}")
print(f"Part 2: {part2Score}")