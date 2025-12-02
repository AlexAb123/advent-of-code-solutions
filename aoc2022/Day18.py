file = open('AoC_input', 'r')
input = file.read().strip().split("\n")
for i in range(len(input)):
    input[i] = input[i].split(",")
for i in range(len(input)):
    for j in range(len(input[i])):
        input[i][j] = int(input[i][j])
surfaceArea = len(input)*6
for i in input:
    x = i[0]
    y = i[1]
    z = i[2]
    for j in input:
        if j != i:
            x1 = j[0]
            y1 = j[1]
            z1 = j[2]
            if x1 == x and y1 == y and (z1+1 == z or z1-1 == z):
                surfaceArea -=1
            if x1 == x and z1 == z and (y1+1 == y or y1-1 == y):
                surfaceArea -=1
            if z1 == z and y1 == y and (x1+1 == x or x1-1 == x):
                surfaceArea -=1
print(f"Part 1: {surfaceArea}")
maxx = 0
minx = input[0][0]
maxy = 0
miny = input[0][1]
maxz = 0
minz = input[0][2]
for i in input:
    if i[0] > maxx:
        maxx = i[0]
    if i[1] > maxy:
        maxy = i[1]
    if i[2] > maxz:
        maxz = i[2]
    if i[0] < minx:
        minx = i[0]
    if i[1] < miny:
        miny = i[1]
    if i[2] < minz:
        minz = i[2]
def isSurrounded(point,input):
    maxx = 0
    minx = input[0][0]
    maxy = 0
    miny = input[0][1]
    maxz = 0
    minz = input[0][2]
    for i in input:
        if i[0] > maxx:
            maxx = i[0]
        if i[1] > maxy:
            maxy = i[1]
        if i[2] > maxz:
            maxz = i[2]
        if i[0] < minx:
            minx = i[0]
        if i[1] < miny:
            miny = i[1]
        if i[2] < minz:
            minz = i[2]
    xCheck1 = False
    yCheck1 = False
    zCheck1 = False
    xCheck2 = False
    yCheck2 = False
    zCheck2 = False
    for x in range(point[0],maxx+1):
        if [x, point[1], point[2]] in input:
            xCheck1 = True
    for y in range(point[1],maxy+1):
        if [point[0], y, point[2]] in input:
            yCheck1 = True
    for z in range(point[2],maxz+1):
        if [point[0], point[1], z] in input:
            zCheck1 = True
    for x in range(minx,point[0]):
        if [x, point[1], point[2]] in input:
            xCheck2 = True
    for y in range(miny,point[1]):
        if [point[0], y, point[2]] in input:
            yCheck2 = True
    for z in range(minz,point[2]):
        if [point[0], point[1], z] in input:
            zCheck2 = True
    if xCheck1 and xCheck2 and yCheck1 and yCheck2 and zCheck1 and zCheck2:
        return True
    else:
        return False
for x in range(minx,maxx+1):
    for y in range(miny,maxy+1):
        for z in range(minz,maxz+1):
            if [x,y,z] not in input:
                if isSurrounded([x,y,z],input):
                    for j in input:
                        x2 = j[0]
                        y2 = j[1]
                        z2 = j[2]
                        if x2 == x and y2 == y and (z2 + 1 == z or z2 - 1 == z):
                            surfaceArea -= 1
                        if x2 == x and z2 == z and (y2 + 1 == y or y2 - 1 == y):
                            surfaceArea -= 1
                        if z2 == z and y2 == y and (x2 + 1 == x or x2 - 1 == x):
                            surfaceArea -= 1
print(f"Part 2: {surfaceArea}")