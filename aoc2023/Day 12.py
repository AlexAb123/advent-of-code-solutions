from pathlib import Path
import time

lines = Path(__file__).with_name('day 12 input.txt').open('r').read().strip().split("\n")
lines = [lines[i].split(" ") for i in range(len(lines))]
lines = [[lines[i][0], list(map(int,lines[i][1].split(",")))] for i in range(len(lines))]

recursiveCalls = 0
cached = 0
cache = {}
def getAllWays(stringLeft, groupsLeft, hashtagCounter=0):
    key = (stringLeft, groupsLeft, hashtagCounter)
    if key in cache:
        global cached
        cached += 1
        return cache[key]
        
    global recursiveCalls
    recursiveCalls += 1

    if len(groupsLeft) == 0:
        return "#" not in stringLeft
    elif len(stringLeft) == 0 and len(groupsLeft) == 0:
        return 1
    elif len(stringLeft) == 0 and len(groupsLeft) == 1 and groupsLeft[0] == hashtagCounter:
        return 1
    elif (len(stringLeft) == 0 and len(groupsLeft) != 0):
        return 0
    elif stringLeft[0] == "?":
        if hashtagCounter == groupsLeft[0]:
            cache[key] = getAllWays(stringLeft[1:], groupsLeft[1:], 0)
            return cache[key]
        elif hashtagCounter < groupsLeft[0] and hashtagCounter != 0:
            cache[key] = getAllWays(stringLeft[1:], groupsLeft, hashtagCounter+1)
            return cache[key]
        elif hashtagCounter == 0:
            cache[key] = getAllWays(stringLeft[1:], groupsLeft, 0) + getAllWays(stringLeft[1:], groupsLeft, hashtagCounter+1)
            return cache[key]

    elif stringLeft[0] == "#":
        if hashtagCounter == groupsLeft[0]:
            cache[key] = 0
            return cache[key]
        elif hashtagCounter < groupsLeft[0]:
            cache[key] = getAllWays(stringLeft[1:], groupsLeft, hashtagCounter + 1)
            return cache[key]

    elif stringLeft[0] == ".":
        if hashtagCounter == groupsLeft[0]:
            cache[key] = getAllWays(stringLeft[1:], groupsLeft[1:], 0)
            return cache[key]
        elif hashtagCounter == 0:
            cache[key] = getAllWays(stringLeft[1:], groupsLeft, 0)
            return cache[key]
        else:
            return 0

startTime = time.time()
part1Score = 0
part2Score = 0
for row, nums in lines:
    part1Score += getAllWays(row, tuple(nums))
    part2Score += getAllWays("?".join([row]*5), tuple(nums*5))
    cache = {}

print(f"Part 1: {part1Score}\nPart 2: {part2Score}")
print(f"\nTime Taken: {(time.time() - startTime)*100//1/100}")
print(f"Recursed {recursiveCalls} times")
print(f"Cache accessed {cached} times")