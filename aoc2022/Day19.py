#PART 2
file = open('aoc_2022/AoC_input.txt', 'r')
input = file.read().strip().split("\n")

blueprints = []
for line in input:
    line = line.split("costs")
    oreCost = int(line[1].split("ore")[0].strip())
    clayCost = int(line[2].split("ore")[0].strip())
    obsidianCost = (int(line[3].split("ore")[0].strip()),int(line[3].split()[3].strip()))
    geodeCost = (int(line[4].split()[0].strip()),int(line[4].split()[3].strip()))
    blueprints.append((oreCost,clayCost,obsidianCost,geodeCost))

qualityLevel = []
cache = {}
def maximiseGeodes(blueprint,oreRobots,clayRobots,obsidianRobots,geodeRobots,ore,clay,obsidian,geodes,timeLeft):
    if (blueprint,oreRobots,clayRobots,obsidianRobots,geodeRobots,ore,clay,obsidian,geodes,timeLeft) in cache:
        return cache[(blueprint,oreRobots,clayRobots,obsidianRobots,geodeRobots,ore,clay,obsidian,geodes,timeLeft)]

    oreCost = blueprint[0]
    clayCost = blueprint[1]
    obsidianCost = blueprint[2]
    geodeCost = blueprint[3]

    oreSpend = max(oreCost,clayCost,obsidianCost[0],geodeCost[0])
    claySpend = obsidianCost[1]
    obsidianSpend = geodeCost[1]

    if ore > oreSpend*timeLeft:
        ore = oreSpend*timeLeft
    if clay > claySpend*timeLeft:
        clay = claySpend*timeLeft
    if obsidian > obsidianSpend*timeLeft:
        obsidian = obsidianSpend*timeLeft

    # print(f"timeLeft: {timeLeft}")
    # print()
    # print(f"Ore: {ore}")
    # print(f"Clay: {clay}")
    # print(f"Obsidian: {obsidian}")
    # print(f"Geodes: {geodes}")
    # print()
    # print(f"OreRobots: {oreRobots}")
    # print(f"ClayRobots: {clayRobots}")
    # print(f"ObsidianRobots: {obsidianRobots}")
    # print(f"GeodeRobots: {geodeRobots}")

    possibleGeodes = []
    possibleGeodes.append(geodes)
    if timeLeft == 0:
        cache[(blueprint,oreRobots,clayRobots,obsidianRobots,geodeRobots,ore,clay,obsidian,geodes,timeLeft)] = max(possibleGeodes)
        return max(possibleGeodes)

    # print(possibleGeodes)
    if ore >= geodeCost[0] and obsidian >= geodeCost[1]:
        possibleGeodes.append(maximiseGeodes(blueprint, oreRobots, clayRobots, obsidianRobots, geodeRobots + 1, ore - geodeCost[0]+oreRobots, clay+clayRobots, obsidian - geodeCost[1]+obsidianRobots, geodes+geodeRobots, timeLeft - 1))

    else:

        if ore >= oreCost and oreRobots < oreSpend:

            possibleGeodes.append(maximiseGeodes(blueprint, oreRobots + 1, clayRobots, obsidianRobots, geodeRobots, ore - oreCost+oreRobots, clay+clayRobots,obsidian+obsidianRobots, geodes+geodeRobots, timeLeft - 1))

        if ore >= clayCost and clayRobots < claySpend:

            possibleGeodes.append(maximiseGeodes(blueprint, oreRobots, clayRobots + 1, obsidianRobots, geodeRobots, ore - clayCost+oreRobots, clay+clayRobots,obsidian+obsidianRobots, geodes+geodeRobots, timeLeft - 1))

        if ore >= obsidianCost[0] and clay >= obsidianCost[1] and obsidianRobots < obsidianSpend:

            possibleGeodes.append(maximiseGeodes(blueprint, oreRobots, clayRobots, obsidianRobots + 1, geodeRobots, ore - obsidianCost[0]+oreRobots,clay - obsidianCost[1]+clayRobots, obsidian+obsidianRobots, geodes+geodeRobots, timeLeft - 1))

        else:
            possibleGeodes.append(maximiseGeodes(blueprint, oreRobots, clayRobots, obsidianRobots, geodeRobots, ore+oreRobots, clay+clayRobots, obsidian+obsidianRobots, geodes+geodeRobots, timeLeft-1))

    # print("--------------------------------------------------------------------------------------------------------------------")
    cache[(blueprint, oreRobots, clayRobots, obsidianRobots, geodeRobots, ore, clay, obsidian, geodes, timeLeft)] = max(possibleGeodes)
    return max(possibleGeodes)

total = 1
for i in range(len(blueprints)):
    print(f"Blueprint {i+1} Started...")
    geode = maximiseGeodes(blueprints[i], 1, 0, 0, 0, 0, 0, 0, 0, 32)
    total = total * geode
    print(f"Blueprint {i+1}: {geode}")
print(total)


#PART 1
'''import math
import itertools
from Library import *

# Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
# Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.

file = open('AoC_input', 'r')
input = file.read().strip().split("\n")

blueprints = []
for line in input:
    line = line.split("costs")
    oreCost = int(line[1].split("ore")[0].strip())
    clayCost = int(line[2].split("ore")[0].strip())
    obsidianCost = (int(line[3].split("ore")[0].strip()),int(line[3].split()[3].strip()))
    geodeCost = (int(line[4].split()[0].strip()),int(line[4].split()[3].strip()))
    blueprints.append((oreCost,clayCost,obsidianCost,geodeCost))

qualityLevel = []
cache = {}
def maximiseGeodes(blueprint,oreRobots,clayRobots,obsidianRobots,geodeRobots,ore,clay,obsidian,geodes,timeLeft):
    if (blueprint,oreRobots,clayRobots,obsidianRobots,geodeRobots,ore,clay,obsidian,geodes,timeLeft) in cache:
        return cache[(blueprint,oreRobots,clayRobots,obsidianRobots,geodeRobots,ore,clay,obsidian,geodes,timeLeft)]

    oreCost = blueprint[0]
    clayCost = blueprint[1]
    obsidianCost = blueprint[2]
    geodeCost = blueprint[3]

    oreSpend = max(oreCost,clayCost,obsidianCost[0],geodeCost[0])
    claySpend = obsidianCost[1]
    obsidianSpend = geodeCost[1]

    # print(f"timeLeft: {timeLeft}")
    # print()
    # print(f"Ore: {ore}")
    # print(f"Clay: {clay}")
    # print(f"Obsidian: {obsidian}")
    # print(f"Geodes: {geodes}")
    # print()
    # print(f"OreRobots: {oreRobots}")
    # print(f"ClayRobots: {clayRobots}")
    # print(f"ObsidianRobots: {obsidianRobots}")
    # print(f"GeodeRobots: {geodeRobots}")

    possibleGeodes = []
    possibleGeodes.append(geodes)
    if timeLeft == 0:
        cache[(blueprint,oreRobots,clayRobots,obsidianRobots,geodeRobots,ore,clay,obsidian,geodes,timeLeft)] = max(possibleGeodes)
        return max(possibleGeodes)

    # print(possibleGeodes)
    if ore >= geodeCost[0] and obsidian >= geodeCost[1]:
        possibleGeodes.append(maximiseGeodes(blueprint, oreRobots, clayRobots, obsidianRobots, geodeRobots + 1, ore - geodeCost[0]+oreRobots, clay+clayRobots, obsidian - geodeCost[1]+obsidianRobots, geodes+geodeRobots, timeLeft - 1))

    else:

        if ore >= oreCost and oreRobots < oreSpend:

            possibleGeodes.append(maximiseGeodes(blueprint, oreRobots + 1, clayRobots, obsidianRobots, geodeRobots, ore - oreCost+oreRobots, clay+clayRobots,obsidian+obsidianRobots, geodes+geodeRobots, timeLeft - 1))

        if ore >= clayCost and clayRobots < claySpend:

            possibleGeodes.append(maximiseGeodes(blueprint, oreRobots, clayRobots + 1, obsidianRobots, geodeRobots, ore - clayCost+oreRobots, clay+clayRobots,obsidian+obsidianRobots, geodes+geodeRobots, timeLeft - 1))

        if ore >= obsidianCost[0] and clay >= obsidianCost[1] and obsidianRobots < obsidianSpend:

            possibleGeodes.append(maximiseGeodes(blueprint, oreRobots, clayRobots, obsidianRobots + 1, geodeRobots, ore - obsidianCost[0]+oreRobots,clay - obsidianCost[1]+clayRobots, obsidian+obsidianRobots, geodes+geodeRobots, timeLeft - 1))

        else:
            possibleGeodes.append(maximiseGeodes(blueprint, oreRobots, clayRobots, obsidianRobots, geodeRobots, ore+oreRobots, clay+clayRobots, obsidian+obsidianRobots, geodes+geodeRobots, timeLeft-1))

    # print("--------------------------------------------------------------------------------------------------------------------")
    cache[(blueprint, oreRobots, clayRobots, obsidianRobots, geodeRobots, ore, clay, obsidian, geodes, timeLeft)] = max(possibleGeodes)
    return max(possibleGeodes)

print("FINAL",maximiseGeodes(blueprints[0],1,0,0,0,0,0,0,0,24))


for i in range(len(blueprints)):
    print(f"Blueprint {i+1}")
    quality = maximiseGeodes(blueprints[i],1,0,0,0,0,0,0,0,32)*(i+1)
    qualityLevel.append(quality)
print("asd")
total = 0
for i in qualityLevel:
    total = total + i
print(total)
'''