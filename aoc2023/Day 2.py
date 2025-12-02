import sys
sys.path.append("Python")
from Library import *

lines = open('Python/Advent_of_Code/AOC2023/day 2 input.txt', 'r').read().strip().split("\n")
lines = [[line.split(":")[0], line.split(":")[1].split(";")] for line in lines]

total1 = 0
total2 = 0
for line in lines:
    id = int(line[0][5:])
    broke = False
    maxB = 0
    maxR = 0
    maxG = 0
    for game in line[1]:
        subGame = game.split(",")
        for numColor in subGame:
            if "green" in numColor:
                count = int((numColor.split(" "))[1])
                if count > maxG:
                    maxG = count
                if count > 13:
                    broke = True
            if "blue" in numColor:
                count = int((numColor.split(" "))[1])
                if count > maxB:
                    maxB = count
                if count > 14:
                    broke = True
            if "red" in numColor:
                count = int((numColor.split(" "))[1])
                if count > maxR:
                    maxR = count
                if count > 12:
                    broke = True
    if not broke:
        total1 += id
    power = maxR * maxB * maxG
    total2 += power

print("Part 1: " + str(total1))
print("Part 2: " + str(total2))