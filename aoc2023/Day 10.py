from pathlib import Path
import copy
lines = Path(__file__).with_name('day 10 input.txt').open('r').read().strip().split("\n")

start = (0,0)
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "S":
            start = (i,j)
distances = []
for i in range(len(lines)):
    temp = []
    for j in range(len(lines[i])):
        temp.append(float("inf"))
    distances.append(temp)

def getAdjacent(row, col, character):
    if character == "|":
        return [(row+1,col),(row-1,col)]
    elif character == "-":
        return [(row,col+1),(row,col-1)]
    elif character == "L":
        return [(row-1,col),(row,col+1)]
    elif character == "J":
        return [(row-1,col),(row,col-1)]
    elif character == "7":
        return [(row+1,col),(row,col-1)]
    elif character == "F":
        return [(row,col+1),(row+1,col)]
    else:
        return [(-1,-1)]

startAdjacents = set()
for row in [-1,0,1]:
    for col in [-1,0,1]:
        r,c = start[0]+row,start[1]+col
        sr, sc = start
        character = lines[r][c]
        if r < len(lines) and c < len(lines[0]):
            if character == "|" and (c == sc and (r == sr-1 or r == sr+1)):
                startAdjacents.add((row,col))
            elif character == "-" and (r == sr and (c == sc-1 or c == sc+1)):
                startAdjacents.add((row,col))
            elif character == "L" and ((r == sr and c+1 == sc) or (c == sc and r == sr+1)):
                startAdjacents.add((row,col))
            elif character == "J" and ((r == sr and c-1 == sc) or (c == sc and r == sr+1)):
                startAdjacents.add((row,col))
            elif character == "7" and ((r+1 == sr and c == sc) or (c == sc+1 and r == sr)):
                startAdjacents.add((row,col))
            elif character == "F" and ((r+1 == sr and c == sc) or (c == sc-1 and r == sr)):
                startAdjacents.add((row,col))

unvisited = set()
for row in range(len(lines)):
    for col in range(len(lines[0])):
        if lines[row][col] != "." and lines[row][col] != "S": 
            unvisited.add((row,col))

distances[start[0]][start[1]] = 0

q = []
for sa in startAdjacents:
    r,c = sa
    pos = (r + start[0], c + start[1])
    q.append(pos)
    distances[pos[0]][pos[1]] = 1
currentPos = ()
while len(q) > 0:
    currentPos = q.pop(0)
    row, col = currentPos
    for adj in getAdjacent(row, col, lines[row][col]):
        if adj != (-1,-1) and adj in unvisited:
            q.append(adj)
            unvisited.remove(currentPos)
            if distances[adj[0]][adj[1]] > distances[row][col]+1:
                distances[adj[0]][adj[1]] = distances[row][col]+1

for i in range(len(distances)):
    distances[i] = list(filter(lambda x: x != float("inf"), distances[i]))
maxd = []
for d in distances:
    if len(d) > 0:
        maxd.append(max(d))

#----------------------------------------------------------------------------------------------
#Part 2:

#Create a grid that is double the size
grid = [["." for j in range(len(lines[0])*2)] for i in range(len(lines)*2)]
for i in range(len(lines)):
    for j in range(len(lines[i])):
        grid[i*2][j*2] = lines[i][j]

#Fill in the spots fo the pipes
tempGrid = copy.deepcopy(grid)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "|":
            tempGrid[i+1][j] = "|"
            tempGrid[i-1][j] = "|"
        if grid[i][j] == "-":
            tempGrid[i][j+1] = "-"
            tempGrid[i][j-1] = "-"
        if grid[i][j] == "F":
            tempGrid[i][j+1] = "-"
            tempGrid[i+1][j] = "|"
        if grid[i][j] == "J":
            tempGrid[i][j-1] = "-"
            tempGrid[i-1][j] = "|"
        if grid[i][j] == "L":
            tempGrid[i][j+1] = "-"
            tempGrid[i-1][j] = "|"
        if grid[i][j] == "7":
            tempGrid[i][j-1] = "-"
            tempGrid[i+1][j] = "-"
        
grid = tempGrid

start = (0,0)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            start = (i,j)

loop = set()
loop.add(start)
unvisited = set()
q = []
for sa in startAdjacents:
    r,c = sa
    pos = (r + start[0], c + start[1])
    q.append(pos)
currentPos = ()

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] != "." and grid[row][col] != "S": 
            unvisited.add((row,col))

while len(q) > 0:
    currentPos = q.pop(0)
    row, col = currentPos
    for adj in getAdjacent(row, col, grid[row][col]):
        if adj != (-1,-1) and adj in unvisited:
            q.append(adj)
            unvisited.remove(adj)
            loop.add(adj)
#set of all points that aren't in the loop
unvisited = set()
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if (row,col) not in loop:
            unvisited.add((row,col))


q = []
area = 0
currentPos = None

#Start at the 4 corners
q.append((0,0))
q.append((len(grid)-1,0))
q.append((0,len(grid[0])-1))
q.append((len(grid)-1,len(grid[0])-1))
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if (r,c) not in loop:
            grid[r][c] = "#"
while len(q) > 0:
    currentPos = q.pop(0)
    row, col = currentPos
    for r in [-1,0,1]:
        for c in [-1,0,1]:
            adj = (row+r,col+c)
            if adj not in loop and adj in unvisited:
                q.append(adj)
                unvisited.remove(adj)
                grid[adj[0]][adj[1]] = "."

area = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if i%2 == 0 and j%2 == 0 and grid[i][j] == "#":
            area +=1

print(f"Part 1: {max(maxd)}")
print(f"Part 2: {area}")