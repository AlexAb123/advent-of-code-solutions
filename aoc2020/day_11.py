from pathlib import Path
lines = Path(__file__).with_name('day_11_input.txt').open('r').read().strip().split("\n")

empty = set()
occupied = set()

for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] == "L":
            empty.add((r,c))
        elif lines[r][c] == "#":
            occupied.add((r,c))

def getAdjacents(pos):
    adjacents = []
    for r in [-1,0,1]:
        for c in[-1,0,1]:
            if not (r == 0 and c == 0) and 0 <= pos[0]+r < len(lines) and 0 <= pos[1]+c < len(lines[0]):
                adjacents.append((pos[0]+r, pos[1]+c))
    return adjacents

def getOccupiedAdjacents(pos):
    occ = 0
    for adj in getAdjacents(pos):
        if adj in occupied:
            occ += 1
    return occ

originalOccupied = occupied.copy()
originalEmpty = empty.copy()

prevOccupied = None
while prevOccupied != occupied:
    newEmpty = empty.copy()
    newOccupied = occupied.copy()
    for seat in empty:
        if getOccupiedAdjacents(seat) == 0:
            newEmpty.remove(seat)
            newOccupied.add(seat)

    for seat in occupied:
        if getOccupiedAdjacents(seat) >= 4:
            newEmpty.add(seat)
            newOccupied.remove(seat)
    
    prevOccupied = occupied
    occupied = newOccupied
    empty = newEmpty

print(f"Part 1: {len(occupied)}")

def getFirstSeatInAllDirections(pos):
    adjacents = []

    for r in [-1,0,1]:
        for c in[-1,0,1]:
            if not (r == 0 and c == 0):

                i = 1
                newPos = (pos[0]+(r*i), pos[1]+(c*i))

                while 0 <= newPos[0] < len(lines) and 0 <= newPos[1] < len(lines[0]):
                    newPos = (pos[0]+(r*i), pos[1]+(c*i))
                    if newPos in occupied or newPos in empty:
                        adjacents.append(newPos)
                        break
                    i += 1
    return adjacents

def getOccupiedAllDirections(pos):
    occ = 0
    for adj in getFirstSeatInAllDirections(pos):
        if adj in occupied:
            occ += 1
    return occ

occupied = originalOccupied
empty = originalEmpty

prevOccupied = None
while prevOccupied != occupied:
    newEmpty = empty.copy()
    newOccupied = occupied.copy()
    for seat in empty:
        if getOccupiedAllDirections(seat) == 0:
            newEmpty.remove(seat)
            newOccupied.add(seat)

    for seat in occupied:
        if getOccupiedAllDirections(seat) >= 5:
            newEmpty.add(seat)
            newOccupied.remove(seat)
    
    prevOccupied = occupied
    occupied = newOccupied
    empty = newEmpty
    
print(f"Part 2: {len(occupied)}")