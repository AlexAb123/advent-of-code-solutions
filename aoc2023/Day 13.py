from pathlib import Path
lines = Path(__file__).with_name('day 13 input.txt').open('r').read().strip().split("\n")

def getColumn(lst, col):
    column = []
    for r in range(len(lst)):
            column.append(lst[r][col])
    return column

def getRow(lst, row):
    return lst[row]

def checkOffByOne(lst1, lst2):
    differences = 0
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            differences += 1
    return differences

def checkSymmetryRow(lst):
    for center in range(len(lst)-1):
        width = min(center+1, len(lst)-center-1)
        start = center+1-width
        end = center+width
        sym = True
        for i in range(width):
            if getRow(lst, start+i) != getRow(lst, end-i):
                sym = False
                break
        if sym:
            return center+1
    return 0

def checkSymmetryCol(lst):
    for center in range(len(lst[0])-1):
        width = min(center+1, len(lst[0])-center-1)
        start = center+1 - width
        end = center+width
        sym = True
        for i in range(width):

            if getColumn(lst, start+i) != getColumn(lst, end-i):
                sym = False
                break
        if sym:
            return center+1
    return 0

def checkSymmetryRowSmudge(lst, oldCenter):
    for center in range(len(lst)-1):
        if center != oldCenter:
            width = min(center+1, len(lst)-center-1)
            start = center+1-width
            end = center+width
            sym = True
            for i in range(width):
                row1 = getRow(lst, start+i)
                row2 = getRow(lst, end-i)
                if checkOffByOne(row1, row2) > 1:
                    sym = False
                    break
            if sym:
                return center+1
    return 0

def checkSymmetryColSmudge(lst, oldCenter):
    for center in range(len(lst[0])-1):
        if center != oldCenter:
            width = min(center+1, len(lst[0])-center-1)
            start = center+1 - width
            end = center+width
            sym = True
            for i in range(width):
                col1 = getColumn(lst, start+i)
                col2 = getColumn(lst, end-i)
                if checkOffByOne(col1, col2) > 1:
                    sym = False
                    break
            if sym:
                return center+1
    return 0

newLines = []
temp = []
for line in lines:
    if line != "":
        temp.append(line)
    else:
        newLines.append(temp)
        temp = []
newLines.append(temp)
lines = newLines

part1Score = 0
part2Score = 0
oldCenters = []
for line in range(len(lines)):
    oldCenters.append((checkSymmetryRow(lines[line])-1, checkSymmetryCol(lines[line])-1))
for line in range(len(lines)):
    part1Score += 100 * checkSymmetryRow(lines[line])
    part1Score += checkSymmetryCol(lines[line])
    part2Score += 100 * (checkSymmetryRowSmudge(lines[line], oldCenters[line][0]))
    part2Score += checkSymmetryColSmudge(lines[line], oldCenters[line][1])

print(f"Part 1: {part1Score}\nPart 2: {part2Score}")