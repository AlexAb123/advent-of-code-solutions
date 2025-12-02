from collections import defaultdict
from math import lcm

file = open('Advent-of-Code/AOC2023/day 8 input.txt', 'r')
input = file.read().strip().split("\n")


instructions = []
for i in input[0]:
    if i == "L":
        instructions.append(0)
    elif i == "R":
        instructions.append(1)

nodes = [input[i].split("=") for i in range(2, len(input))]
for i in range(len(nodes)):
    for j in range(len(nodes[i])):
        nodes[i][j] = nodes[i][j].strip()
        nodes[i][j] = nodes[i][j].replace("(", "")
        nodes[i][j] = nodes[i][j].replace(")", "")
        nodes[i][j] = nodes[i][j].split(", ")
        
nodeDict = defaultdict(list)
for n in nodes:
    nodeDict[n[0][0]] = n[1]

currentNode = "AAA"
steps = 0
i = 0
while True:
    currentNode = nodeDict[currentNode][instructions[i]]
    steps += 1
    if currentNode == "ZZZ":
        break
    if i < len(instructions)-1:
        i += 1
    else:
        i = 0
print(f"Part 1: {steps}")

startingNodes = []
for n in nodes:
    if n[0][0][2] == "A":
        startingNodes.append(n[0][0])

nodeSteps = []
for currentNode in startingNodes:
    steps = 0
    i = 0
    while True:
        currentNode = nodeDict[currentNode][instructions[i]]
        steps += 1
        if currentNode[2] == "Z":
            break
        if i < len(instructions)-1:
            i += 1
        else:
            i = 0
    nodeSteps.append(steps)
LCM = 1
for i in nodeSteps:
    LCM = lcm(LCM,i)
print(f"Part 2: {LCM}")