import itertools
import math

def minRow(s):
    m = 999999999999
    for i in s:
        if i[0] < m:
            m = i[0]
    return m
def minCol(s):
    m = 999999999999
    for i in s:
        if i[1] < m:
            m = i[1]
    return m
def maxRow(s):
    m = -999999999999
    for i in s:
        if i[0] > m:
            m = i[0]
    return m
def maxCol(s):
    m = -999999999999
    for i in s:
        if i[1] > m:
            m = i[1]
    return m

def vis():
    out = []
    for row in range(minRow(elves), maxRow(elves) + 1):
        temp = ""
        for col in range(minCol(elves), maxCol(elves) + 1):
            if (row, col) in elves:
                temp = temp + "#"
            else:
                temp = temp + "."
        out.append(temp)
    for i in out:
        print(i)

file = open("AoC_input", "r")
input = file.read().strip().split("\n")

elves = set()
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "#":
            elves.add((i+1,j+1))

def hasNeighbour(pos):
    x = pos[0]
    y = pos[1]
    if (x+1,y) in elves:
        return True
    elif (x-1,y) in elves:
        return True
    elif (x,y+1) in elves:
        return True
    elif (x,y-1) in elves:
        return True
    elif (x+1,y+1) in elves:
        return True
    elif (x+1,y-1) in elves:
        return True
    elif (x-1,y+1) in elves:
        return True
    elif (x-1,y-1) in elves:
        return True

def hasDir(pos,dir):
    x = pos[0]
    y = pos[1]
    if dir == "n":
        if (x-1,y) not in elves and (x-1,y-1) not in elves and (x-1,y+1) not in elves:
            return False
    elif dir == "s":
        if (x+1,y) not in elves and (x+1,y+1) not in elves and (x+1,y-1) not in elves:
            return False
    elif dir == "e":
        if (x,y+1) not in elves and (x+1,y+1) not in elves and (x-1,y+1) not in elves:
            return False
    elif dir == "w":
        if (x,y-1) not in elves and (x-1,y-1) not in elves and (x+1,y-1) not in elves:
            return False

    return True


propose = ["n","s","w","e"]

elfMoves = {}
prev = None
count = 1
while True:

    elfMoves = {}
    # print(f"Round {i+1} Starting")
    for elf in elves:
        # print(elfMoves)
        x = elf[0]
        y = elf[1]

        if hasNeighbour(elf):
            for prop in propose:

                if not hasDir(elf,prop):
                    if prop == "n":
                        if (x-1,y) not in elfMoves:
                            elfMoves[(x-1,y)] = [elf]
                        else:
                            elfMoves[(x-1,y)].append(elf)


                    elif prop == "s":
                        if (x+1,y) not in elfMoves:
                            elfMoves[(x+1,y)] = [elf]
                        else:
                            elfMoves[(x+1,y)].append(elf)


                    elif prop == "e":
                        if (x,y+1) not in elfMoves:
                            elfMoves[(x,y+1)] = [elf]
                        else:
                            elfMoves[(x,y+1)].append(elf)


                    elif prop == "w":
                        if (x,y-1) not in elfMoves:
                            elfMoves[(x,y-1)] = [elf]
                        else:
                            elfMoves[(x,y-1)].append(elf)
                    break
    moved = False
    for move in elfMoves:
        if len(elfMoves[move]) == 1:

            elves.remove(elfMoves[move][0])
            elves.add(move)
            moved = True
    if not moved:
        print(count)
        break
    else:
        count+=1

    propose.append(propose.pop(0))



'''import itertools
import math

def minRow(s):
    m = 999999999999
    for i in s:
        if i[0] < m:
            m = i[0]
    return m
def minCol(s):
    m = 999999999999
    for i in s:
        if i[1] < m:
            m = i[1]
    return m
def maxRow(s):
    m = -999999999999
    for i in s:
        if i[0] > m:
            m = i[0]
    return m
def maxCol(s):
    m = -999999999999
    for i in s:
        if i[1] > m:
            m = i[1]
    return m

def vis():
    out = []
    for row in range(minRow(elves), maxRow(elves) + 1):
        temp = ""
        for col in range(minCol(elves), maxCol(elves) + 1):
            if (row, col) in elves:
                temp = temp + "#"
            else:
                temp = temp + "."
        out.append(temp)
    for i in out:
        print(i)

file = open("AoC_input", "r")
input = file.read().strip().split("\n")

elves = set()
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "#":
            elves.add((i+1,j+1))

def hasNeighbour(pos):
    x = pos[0]
    y = pos[1]
    if (x+1,y) in elves:
        return True
    elif (x-1,y) in elves:
        return True
    elif (x,y+1) in elves:
        return True
    elif (x,y-1) in elves:
        return True
    elif (x+1,y+1) in elves:
        return True
    elif (x+1,y-1) in elves:
        return True
    elif (x-1,y+1) in elves:
        return True
    elif (x-1,y-1) in elves:
        return True

def hasDir(pos,dir):
    x = pos[0]
    y = pos[1]
    if dir == "n":
        if (x-1,y) not in elves and (x-1,y-1) not in elves and (x-1,y+1) not in elves:
            return False
    elif dir == "s":
        if (x+1,y) not in elves and (x+1,y+1) not in elves and (x+1,y-1) not in elves:
            return False
    elif dir == "e":
        if (x,y+1) not in elves and (x+1,y+1) not in elves and (x-1,y+1) not in elves:
            return False
    elif dir == "w":
        if (x,y-1) not in elves and (x-1,y-1) not in elves and (x+1,y-1) not in elves:
            return False

    return True


propose = ["n","s","w","e"]

rounds = 10
elfMoves = {}
prev = elves
for i in range(rounds):

    elfMoves = {}
    # print(f"Round {i+1} Starting")
    for elf in elves:
        # print(elfMoves)
        x = elf[0]
        y = elf[1]

        if hasNeighbour(elf):
            for prop in propose:

                if not hasDir(elf,prop):
                    if elf == (5,3):
                        for h in elves:
                            if h[0] == 4:
                                print(h)
                    if prop == "n":
                        if (x-1,y) not in elfMoves:
                            elfMoves[(x-1,y)] = [elf]
                        else:
                            elfMoves[(x-1,y)].append(elf)


                    elif prop == "s":
                        if (x+1,y) not in elfMoves:
                            elfMoves[(x+1,y)] = [elf]
                        else:
                            elfMoves[(x+1,y)].append(elf)


                    elif prop == "e":
                        if (x,y+1) not in elfMoves:
                            elfMoves[(x,y+1)] = [elf]
                        else:
                            elfMoves[(x,y+1)].append(elf)


                    elif prop == "w":
                        if (x,y-1) not in elfMoves:
                            elfMoves[(x,y-1)] = [elf]
                        else:
                            elfMoves[(x,y-1)].append(elf)
                    break

    for move in elfMoves:
        if len(elfMoves[move]) == 1:

            elves.remove(elfMoves[move][0])
            elves.add(move)
    

    
    propose.append(propose.pop(0))


totalArea = (maxRow(elves)-minRow(elves)+1) * (maxCol(elves)-minCol(elves)+1)

print(totalArea-len(elves))'''