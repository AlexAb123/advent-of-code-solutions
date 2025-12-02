import sys
sys.path.append("Python")
from Library import *
from math import floor, ceil

file = open('Python/Advent_of_Code/AOC2023/day 6 input.txt', 'r')
input = file.read().strip().split("\n")

times = [int(i) for i in input[0].split(":")[1].split(" ") if i.isdigit()]
distances = [int(i) for i in input[1].split(":")[1].split(" ") if i.isdigit()]

part1Score = 1
for i in range(len(times)):
    lowerRoot = (-times[i] + ((times[i]**2)-4*distances[i])**0.5)/-2.0
    upperRoot = (-times[i] - ((times[i]**2)-4*distances[i])**0.5)/-2.0
    score = ceil(upperRoot) - floor(lowerRoot) - 1
    part1Score *= score
print(f"Part 1: {part1Score}")

time = ""
dist = ""
for i in range(len(times)):
    time += str(times[i])
    dist += str(distances[i])
time = int(time)
dist = int(dist)

lowerRoot = (-time + ((time**2)-4*dist)**0.5)/-2.0
upperRoot = (-time - ((time**2)-4*dist)**0.5)/-2.0
part2Score = ceil(upperRoot) - floor(lowerRoot) - 1
print(f"Part 2: {part2Score}")