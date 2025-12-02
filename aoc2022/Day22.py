import itertools
import math
from Library import *

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
def minRowatCol(s,c):
    m = 999999999999
    for i in s:
        if i[0] < m and i[1] == c:
            m = i[0]
    return m
def minColatRow(s,r):
    m = 999999999999
    for i in s:
        if i[1] < m and i[0] == r:
            m = i[1]
    return m
def maxRowatCol(s,c):
    m = -999999999999
    for i in s:
        if i[0] > m and i[1] == c:
            m = i[0]
    return m
def maxColatRow(s,r):
    m = -999999999999
    for i in s:
        if i[1] > m and i[0] == r:
            m = i[1]
    return m

file = open('AoC_input', 'r')
input = file.read().split('\n')
inputDir = []
walls = set()
empty = set()

for i in range(len(input)):
    if input[i] == '':
        for j in range(i+1,len(input)):
            inputDir.append(input[j])
        break

    for j in range(len(input[i])):
        if input[i][j] != " ":
            if input[i][j] == ".":
                empty.add((i+1,j+1))
            if input[i][j] == "#":
                walls.add((i+1,j+1))
temp = ""
for i in inputDir:
    temp = temp + i
inputDir = temp
dir = []
temp = ""
for i in range(len(inputDir)):
    if not inputDir[i].isnumeric():
        dir.append(temp)
        temp = ""
        dir.append(inputDir[i])
    else:
        temp = temp + inputDir[i]
if temp != "":
    dir.append(temp)

for i in range(len(dir)):
    if dir[i].isnumeric():
        dir[i] = int(dir[i])


tiles = empty.union(walls)
n = 50
def mod50(a):
    return (a-1)%n

s1 = set()
s2 = set()
s3 = set()
s4 = set()
s5 = set()
s6 = set()

for row in range(1,n+1):
    for col in range(n*2+1,n*3+1):
        if (row,col) in tiles:
            s1.add((row,col))
for row in range(1,n+1):
    for col in range(n+1,n*2+1):
        if (row,col) in tiles:
            s2.add((row,col))
for row in range(n+1,n*2+1):
    for col in range(n+1,n*2+1):
        if (row,col) in tiles:
            s3.add((row,col))
for row in range(n*2,n*3+1):
    for col in range(n+1,n*2+1):
        if (row,col) in tiles:
            s4.add((row,col))
for row in range(n*2+1,n*3+1):
    for col in range(1,n+1):
        if (row,col) in tiles:
            s5.add((row,col))
for row in range(n*3+1,n*4+1):
    for col in range(1,n+1):
        if (row,col) in tiles:
            s6.add((row,col))

input.pop(-1)
input.pop(-1)
face = "R"
pos = (1,minColatRow(empty,1))
print(pos,face)

for i in dir:

    if isinstance(i,str):
        if i == "R":
            if face == "R":
                face = "D"
            elif face == "U":
                face = "R"
            elif face == "L":
                face = "U"
            elif face == "D":
                face = "L"
        elif i == "L":
            if face == "R":
                face = "U"
            elif face == "U":
                face = "L"
            elif face == "L":
                face = "D"
            elif face == "D":
                face = "R"

    elif isinstance(i,int):

        for j in range(1,i+1):
            print(pos, i, face)
            if face == "R":
                if (pos[0],pos[1]+1) in empty and (pos[0],pos[1]+1) not in walls:
                    pos = (pos[0],pos[1]+1)
                elif (pos[0], pos[1] + 1) not in tiles:
                    if pos in s1:
                        if (maxRow(s4) - mod50(pos[0]), maxCol(s4)) not in walls:
                            face = "L"
                            pos = (maxRow(s4)-mod50(pos[0]),maxCol(s4))

                    elif pos in s3:
                        if (maxRow(s1), minCol(s1) + mod50(pos[0])) not in walls:
                            face = "U"
                            pos = (maxRow(s1),minCol(s1)+mod50(pos[0]))

                    elif pos in s4:
                        if (maxRow(s1) - mod50(pos[0]), maxCol(s1)) not in walls:
                            face = "L"
                            pos = (maxRow(s1)-mod50(pos[0]),maxCol(s1))

                    elif pos in s6:
                        if (maxRow(s4), minCol(s4) + mod50(pos[0])) not in walls:
                            face = "U"
                            pos = (maxRow(s4),minCol(s4)+mod50(pos[0]))



            elif face == "U":
                if (pos[0]-1,pos[1]) in empty and (pos[0]-1,pos[1]) not in walls:
                    pos = (pos[0]-1,pos[1])
                elif (pos[0] - 1, pos[1]) not in tiles:
                    if pos in s1:
                        if (maxRow(s6), minCol(s6) + mod50(pos[1])) not in walls:
                            face = "U"
                            pos = (maxRow(s6),minCol(s6)+mod50(pos[1]))

                    elif pos in s2:
                        if (minRow(s6) + mod50(pos[1]), minCol(s6)) not in walls:
                            face = "R"
                            pos = (minRow(s6)+mod50(pos[1]),minCol(s6))

                    elif pos in s5:
                        if (minRow(s3) + mod50(pos[1]), minCol(s3)) not in walls:
                            face = "R"
                            pos = (minRow(s3)+mod50(pos[1]),minCol(s3))

            elif face == "L":
                if (pos[0],pos[1]-1) in empty and (pos[0],pos[1]-1) not in walls:
                    pos = (pos[0],pos[1]-1)
                elif (pos[0], pos[1] - 1) not in tiles:
                    if pos in s2:
                        if (maxRow(s5)-mod50(pos[0]),minCol(s5)) not in walls:
                            face = "R"
                            pos = (maxRow(s5)-mod50(pos[0]),minCol(s5))



                    elif pos in s3:
                        if (minRow(s5), minCol(s5) + mod50(pos[0])) not in walls:
                            face = "D"
                            pos = (minRow(s5),minCol(s5)+mod50(pos[0]))

                    elif pos in s5:
                        if (maxRow(s2)-mod50(pos[0]),minCol(s2)) not in walls:
                            print(f"ad,: {pos[0]}")
                            print(mod50(pos[0]))
                            face = "R"
                            pos = (maxRow(s2)-mod50(pos[0]),minCol(s2))

                    elif pos in s6:
                        if (minRow(s2), minCol(s2) + mod50(pos[0])) not in walls:
                            face = "D"
                            pos = (minRow(s2),minCol(s2)+mod50(pos[0]))

            elif face == "D":
                if (pos[0]+1,pos[1]) in empty and (pos[0]+1,pos[1]) not in walls:
                    pos = (pos[0]+1,pos[1])
                elif (pos[0] + 1, pos[1]) not in tiles:
                    if pos in s1:
                        if (minRow(s3) + mod50(pos[1]), maxCol(s3)) not in walls:
                            face = "L"
                            pos = (minRow(s3)+mod50(pos[1]),maxCol(s3))


                    elif pos in s4:
                        if (minRow(s6) + mod50(pos[1]), maxCol(s6)) not in walls:
                            face = "L"
                            pos = (minRow(s6)+mod50(pos[1]),maxCol(s6))
                    elif pos in s6:
                        if (minRow(s1), minCol(s1) + mod50(pos[1])) not in walls:
                            face = "D"
                            pos = (minRow(s1),minCol(s1)+mod50(pos[1]))




print(pos,face)

if face == "R":
    f = 0
elif face == "D":
    f = 1
elif face == "L":
    f = 2
elif face == "U":
    f = 3

final = (1000*pos[0])+(4*pos[1])+f
print(final)