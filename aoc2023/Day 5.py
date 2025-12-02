import sys
sys.path.append("Python")
from Library import *
from collections import defaultdict

file = open('AOC2023/day 5 input.txt', 'r')
input = file.read().strip().split("\n")

input = [input[i] for i in range(len(input)) if input[i] != ""]
for i in range(len(input)):
    input[i] = input[i].split(":")
for i in range(len(input)):
    if len(input[i]) > 1 and input[i][1] == "": 
        input[i] = [input[i][0]]

mapDict = defaultdict(list)

seeds = input[0][1].strip().split(" ")
current = -1
input.remove(input[0])
for i in input:
    if "-" not in i[0]:
        mapDict[current].append(i[0].split(" "))
    else:
        current += 1
# 0 is destination start
# 1 is source start
# 2 is range
def findCorresponding(seed, layerIndex):
    seed = int(seed)
    for mapp in mapDict[layerIndex]:
        if int(mapp[1]) < seed < int(mapp[1]) + int(mapp[2]):
            return int(mapp[0]) + seed - int(mapp[1])
    return seed

vals = []
for seed in seeds:
    cur = seed
    for i in range(7):
        cur = findCorresponding(cur, i)
    vals.append(cur) 
print(f"Part 1: {min(vals)}")



def applyRanges(ranges, layer):
    final = []
    for d, s, l in mapDict[layer]:
        temp = []
        s2 = int(s)
        e2 = int(s) + int(l)
        translate = int(d) - int(s)
        while ranges:
            
            s1, e1 = ranges.pop()
            left = (s1, min(s2, e1))
            middle = (max(s1, s2), min(e1,e2))
            right = (max(s1, e2), e1)

            if left[1] > left[0]:
                temp.append(left)
            if middle[1] > middle[0]:
                final.append((middle[0]+translate, middle[1]+translate))
            if right[1] > right[0]:
                temp.append(right)

        ranges = temp

    return final + ranges

ranges = []
for i in range(0, len(seeds), 2):
    ranges.append((int(seeds[i]), int(seeds[i+1])+int(seeds[i])))

finalRanges = []
for i in range(8):
    finalRanges.append([])

finalRanges[0] = ranges

for layer in range(7):
    finalRanges[layer+1] = applyRanges(finalRanges[layer],layer)

locations = [r[0] for r in finalRanges[7]]
print(f"Part 2: {min(locations)}")