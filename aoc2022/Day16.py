import math
import itertools
from Library import *

file = open('AOC2022/AoC_input', 'r')
input = file.read().strip().split("\n")
for i in range(len(input)):
    input[i] = input[i].split()
for i in range(len(input)):
    input[i][4] = input[i][4].split("=")
    input[i][4][1] = input[i][4][1].split(";")

class Valve():
    def __init__(self,name,flowRate):
        self.name = name
        self.flowRate = flowRate
        self.minutes = 0
        self.tunnels = None
        self.open = False

    def getName(self):
        return self.name
    def getTunnels(self):
        return self.tunnels
    def setTunnels(self,tunnels):
        self.tunnels = tunnels
    def addTunnel(self,tunnel):
        self.tunnels.append(tunnel)
    def removeDupeTunnel(self):
        for i in range(len(self.tunnels)-1,-1,-1):
            if self.tunnels[i][0] == self:
                self.tunnels.pop(i)
    def getFlowRate(self):
        return self.flowRate
    def getTotalPressure(self):
        return self.minutes * self.flowRate
    def addMinuteIfOpen(self):
        if self.open:
            self.minutes = self.minutes + 1
    def isOpen(self):
        return self.open
    def open(self):
        self.open = True
    def __repr__(self):
        return (f"{self.name}")

def findValve(valves,name):
    for valve in valves:
        if valve.getName() == name:
            return valve
    return f"{name} not found"


valves = set()
for i in input:
    name = i[1]
    flowRate = int(i[4][1][0])
    valves.add(Valve(name,flowRate))

'''creates the length 1 connections'''
connections = []
for i in input:
    t1 = i[1]
    for j in range(len(i)-1,0,-1):
        if i[j] == "valves" or i[j] == "valve":
            break
        t2 = i[j].split(",")[0]
        if [set([t1,t2]),1] not in connections:
            connections.append([set([t1,t2]),1])

def findDistOf(lst,name):
    for i in lst:
        if i[0] == name:
            return i[1]

firstValveName = "AA"
for i in valves:
    con = []
    newCon = []
    newConNames = []
    if i.getFlowRate() == 0 and i.getName() != firstValveName:
        name = i.getName()
        for j in connections:
            if name in j[0]:
                con.append(j)
        for j in con:
            for k in j[0]:
                if k != name:
                    newCon.append([k,j[1]])
                    newConNames.append(k)
        for j in itertools.combinations(newConNames,2):
            add = [set(j),findDistOf(newCon,j[0])+findDistOf(newCon,j[1])]
            for find in range(len(connections)-1,0,-1):
                if name in connections[find][0]:
                    connections.pop(find)
            connections.append(add)

'''Dont know what happens here so just hardcoded it'''
for i in range(len(connections)-1,-1,-1):
    if "TU" in connections[i][0]:
        connections.pop(i)


temp = valves.copy()
for i in temp:
    if i.getFlowRate() == 0 and i.getName() != firstValveName:
        valves.remove(i)
temp = valves.copy()
for i in temp:
    if i.getName() == "TU":
        valves.remove(i)
'''adds tunnels to each valve as [(valve, cost), (valve, cost)]'''
for valve in valves:
    tunnels = []
    for con in connections:
        if valve.getName() in con[0]:
            for name in con[0]:
                if name != valve.getName():
                    tunnels.append((findValve(valves,name),con[1]))
    valve.setTunnels(tunnels)

def bubbleSort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j][1] > lst[j+1][1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst

def replaceQ(q,val,dist):
    found = False
    for i in q:
        if i[0] == val[0]:
            found = True
            if val[1]+dist < i[1]:
                i[1] = val[1]+dist
                break
    if not found:
        q.append(val)
    return

def findDistInList(distList,valve):
    for i in range(len(distList)):
        if distList[i][0] == valve:
            return distList[i][1]

def shortestPath(valve):
    start = valve
    q = [[valve,0]]
    dist = 0
    distList = []
    for i in valves:
        if i == valve:
            distList.append([i,0])
        else:
            distList.append([i,9999999])
    visited = set()
    while len(q) > 0:
        curValve = q[0]
        q.pop(0)
        dist = findDistInList(distList,curValve[0])
        for i in curValve[0].getTunnels():
            val = list(i)
            replaceQ(distList, val, dist)
            if i[0] not in visited:
                q.append((val[0],val[1]+dist))
        visited.add(curValve[0])
        bubbleSort(q)
    start.setTunnels(distList)

for valve in valves:
    shortestPath(valve)
    valve.removeDupeTunnel()

valves = list(valves)
valveIndex = {}
for i in range(len(valves)):
    valveIndex[valves[i]] = i



done = set()
cache = {}
def findMaxPressurePart2(curValve,pressure,open,timeLeft):
    # print(f"curValve: {curValve}")
    # print(f"Pressure: {pressure}")
    # print(f"open: {open}")
    # print(f"timeLeft: {timeLeft} ")
    # print()

    if (curValve, pressure, open, timeLeft) in cache:
        return cache[(curValve, pressure, open, timeLeft)]

    if timeLeft == 0:
        cache[(curValve, pressure, open, timeLeft)] = pressure
        return pressure

    open = list(open)
    open[valveIndex[curValve]] = True
    open = tuple(open)

    possiblePressures = []
    possiblePressures.append(pressure + (curValve.getFlowRate() * timeLeft))

    allOpen = True
    for i in open:
        if not i:
            allOpen = False
    if allOpen:
        return max(possiblePressures)

    for neighbour in curValve.getTunnels():

        if timeLeft - (neighbour[1] + 1) >= 0 and open[valveIndex[neighbour[0]]] == False:
            possiblePressures.append(findMaxPressurePart2(neighbour[0], pressure + (curValve.getFlowRate() * timeLeft), open,
                                                     timeLeft - (neighbour[1] + 1)))

    cache[curValve, pressure, open, timeLeft] = max(possiblePressures)
    return max(possiblePressures)


player1 = []
player2 = []

def disjoint(tup1):
    new = []
    for i in tup1:
        new.append(not i)
    return tuple(new)

def parseBool(str):
    temp = []
    for i in range(len(str)):
        temp.append(bool(int(str[i])))
    return temp

def dectobin(dec,leng):
    bina = str(bin(dec))[2:]
    while len(bina) < leng:
        bina = "0" + bina
    return bina

perms = set()
leng = len(valves)
print(leng)
for i in range(65537):
    temp = parseBool(dectobin(i, leng))
    perms.add((tuple(temp),tuple(disjoint(temp))))
maxs = 0
print(len(perms))
for i in perms:
    maxs = max(findMaxPressurePart2(findValve(valves,"AA"),0,i[0],26) + findMaxPressurePart2(findValve(valves,"AA"),0,i[1],26),maxs)
    print(maxs)
print(maxs)

#PART 1: SOME IS HARDCODED - WONT WORK FOR ALL inputS
'''import math
import itertools
from Library import *

file = open('AoC_input', 'r')
input = file.read().strip().split("\n")
for i in range(len(input)):
    input[i] = input[i].split()
for i in range(len(input)):
    input[i][4] = input[i][4].split("=")
    input[i][4][1] = input[i][4][1].split(";")

class Valve():
    def __init__(self,name,flowRate):
        self.name = name
        self.flowRate = flowRate
        self.minutes = 0
        self.tunnels = None
        self.open = False

    def getName(self):
        return self.name
    def getTunnels(self):
        return self.tunnels
    def setTunnels(self,tunnels):
        self.tunnels = tunnels
    def addTunnel(self,tunnel):
        self.tunnels.append(tunnel)
    def removeDupeTunnel(self):
        for i in range(len(self.tunnels)-1,-1,-1):
            if self.tunnels[i][0] == self:
                self.tunnels.pop(i)
    def getFlowRate(self):
        return self.flowRate
    def getTotalPressure(self):
        return self.minutes * self.flowRate
    def addMinuteIfOpen(self):
        if self.open:
            self.minutes = self.minutes + 1
    def isOpen(self):
        return self.open
    def open(self):
        self.open = True
    def __repr__(self):
        return (f"{self.name}")

def findValve(valves,name):
    for valve in valves:
        if valve.getName() == name:
            return valve
    return f"{name} not found"


valves = set()
for i in input:
    name = i[1]
    flowRate = int(i[4][1][0])
    valves.add(Valve(name,flowRate))

#creates the length 1 connections
connections = []
for i in input:
    t1 = i[1]
    for j in range(len(i)-1,0,-1):
        if i[j] == "valves" or i[j] == "valve":
            break
        t2 = i[j].split(",")[0]
        if [set([t1,t2]),1] not in connections:
            connections.append([set([t1,t2]),1])

def findDistOf(lst,name):
    for i in lst:
        if i[0] == name:
            return i[1]

firstValveName = "AA"
for i in valves:
    con = []
    newCon = []
    newConNames = []
    if i.getFlowRate() == 0 and i.getName() != firstValveName:
        name = i.getName()
        for j in connections:
            if name in j[0]:
                con.append(j)
        for j in con:
            for k in j[0]:
                if k != name:
                    newCon.append([k,j[1]])
                    newConNames.append(k)
        for j in itertools.combinations(newConNames,2):
            add = [set(j),findDistOf(newCon,j[0])+findDistOf(newCon,j[1])]
            for find in range(len(connections)-1,0,-1):
                if name in connections[find][0]:
                    connections.pop(find)
            connections.append(add)

#Dont know what happens here so just hardcoded it
for i in range(len(connections)-1,-1,-1):
    if "TU" in connections[i][0]:
        connections.pop(i)


temp = valves.copy()
for i in temp:
    if i.getFlowRate() == 0 and i.getName() != firstValveName:
        valves.remove(i)
temp = valves.copy()
for i in temp:
    if i.getName() == "TU":
        valves.remove(i)
# adds tunnels to each valve as [(valve, cost), (valve, cost)]
for valve in valves:
    tunnels = []
    for con in connections:
        if valve.getName() in con[0]:
            for name in con[0]:
                if name != valve.getName():
                    tunnels.append((findValve(valves,name),con[1]))
    valve.setTunnels(tunnels)

def bubbleSort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j][1] > lst[j+1][1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst

def replaceQ(q,val,dist):
    found = False
    for i in q:
        if i[0] == val[0]:
            found = True
            if val[1]+dist < i[1]:
                i[1] = val[1]+dist
                break
    if not found:
        q.append(val)
    return

def findDistInList(distList,valve):
    for i in range(len(distList)):
        if distList[i][0] == valve:
            return distList[i][1]

def shortestPath(valve):
    start = valve
    q = [[valve,0]]
    dist = 0
    distList = []
    for i in valves:
        if i == valve:
            distList.append([i,0])
        else:
            distList.append([i,9999999])
    visited = set()
    while len(q) > 0:
        curValve = q[0]
        q.pop(0)
        dist = findDistInList(distList,curValve[0])
        for i in curValve[0].getTunnels():
            val = list(i)
            replaceQ(distList, val, dist)
            if i[0] not in visited:
                q.append((val[0],val[1]+dist))
        visited.add(curValve[0])
        bubbleSort(q)
    start.setTunnels(distList)

for valve in valves:
    shortestPath(valve)
    valve.removeDupeTunnel()

valves = list(valves)
valveIndex = {}
for i in range(len(valves)):
    valveIndex[valves[i]] = i

open = []

for valve in valves:
    open.append(False)
open = tuple(open)

# print(tuple(open))
# open[valveIndex[valve]] = True
# if open[valveIndex[valve]]:
#     then its open
# else:
#     its not open

cache = {}
def findMaxPressure(curValve,pressure,open,timeLeft):
    # print(f"curValve: {curValve}")
    # print(f"Pressure: {pressure}")
    # print(f"open: {open}")
    # print(f"timeLeft: {timeLeft} ")
    # print()

    if (curValve,pressure,open,timeLeft) in cache:

        return cache[(curValve,pressure,open,timeLeft)]

    if timeLeft == 0:
        cache[(curValve, pressure, open, timeLeft)] = pressure
        return pressure

    open = list(open)
    open[valveIndex[curValve]] = True
    open = tuple(open)

    possiblePressures = []
    possiblePressures.append(pressure+(curValve.getFlowRate()*timeLeft))

    allOpen = True
    for i in open:
        if not i:
            allOpen = False
    if allOpen:
        return max(possiblePressures)

    for neighbour in curValve.getTunnels():

        if timeLeft - (neighbour[1]+1) >= 0 and open[valveIndex[neighbour[0]]] == False:

            possiblePressures.append(findMaxPressure(neighbour[0],pressure+(curValve.getFlowRate()*timeLeft),open,timeLeft-(neighbour[1]+1)))


    cache[curValve,pressure,open,timeLeft] = max(possiblePressures)
    return max(possiblePressures)


print(findMaxPressure(findValve(valves,"AA"),0,open,30))'''