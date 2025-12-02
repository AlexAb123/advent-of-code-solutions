import itertools
import math
from Library import *

def moveBlizz(b):
    ret = []
    for i in range(len(b)):
        row = b[i][0][0]
        col = b[i][0][1]
        d = b[i][1]
        if d == ">":
            if (row,col+1) in insideSpots:
                ret.append(((row,col+1),d))
            else:
                ret.append(((row,minCol(insideSpots)),d))
        elif d == "<":
            if (row,col-1) in insideSpots:
                ret.append(((row,col-1),d))
            else:
                ret.append(((row,maxCol(insideSpots)),d))
        elif d == "^":
            if (row-1,col) in insideSpots:
                ret.append(((row-1,col),d))
            else:
                ret.append(((maxRow(insideSpots),col),d))
        elif d == "v":
            if (row+1,col) in insideSpots:
                ret.append(((row+1,col),d))
            else:
                ret.append(((minRow(insideSpots),col),d))

    return tuple(ret)

file = open("AoC_input", "r")
input = file.read().strip().split("\n")

spots = set()
walls = set()
blizz = []
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "#":
            walls.add((i+1,j+1))
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] != "#":
            spots.add((i+1,j+1))
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] != "#" and input[i][j] != "." :
            blizz.append((((i+1,j+1),input[i][j])))
blizz = tuple(blizz)
insideSpots = set()
for i in spots:
    if i[0] != minRow(spots) and i[0] != maxRow(spots):
        insideSpots.add(i)

period = math.lcm((len(input)-2),(len(input[0])-2))

blizzStates = {}
blizzStates[0] = blizz
for i in range(1,period):
    blizzStates[i] = moveBlizz(blizzStates[i-1])

states = []
for i in blizzStates.values():
    temp = set()
    for j in i:
        temp.add(j[0])
    states.append(temp)

start = None
end = None
for i in spots:
    if i[0] == minRow(spots):
        start = i

    if i[0] == maxRow(spots):
        end = i
row = start[0]
col = start[1]

def adjacent(p):
    n = set()
    row = p[0]
    col = p[1]
    n.add((row-1,col))
    n.add((row+1,col))
    n.add((row,col-1))
    n.add((row,col+1))
    return n


#Dijkstra's Algorithm
def leastTime(s,e,t):
    q = [(s, t)]
    visited = set()
    pos = None
    target = e
    while len(q)>0:

         pos = q[0][0]
         time = q[0][1]
         if pos == target:
             return(time)
             break

         q.pop(0)

         neighbours = adjacent(pos)
         neighbours.add(pos)


         for n in neighbours:
             newState = (n,(time+1)%period)

             if newState not in visited and n not in states[newState[1]] and n in spots:
                 if (n,time+1) not in q:
                    q.append((n,time+1))
                    visited.add(newState)


p1 = leastTime(start,end,0)
print(f"Part 1: {p1}")
print()
p2 = leastTime(start,end,leastTime(end,start,p1))
print(f"Part 2: {p2}")