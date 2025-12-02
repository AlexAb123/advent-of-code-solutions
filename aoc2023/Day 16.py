from pathlib import Path
lines = Path(__file__).with_name('day 16 input.txt').open('r').read().strip().split("\n")

def inBounds(pos):
    return pos[0] >= 0 and pos[0] < len(lines) and pos[1] >= 0 and pos[1] < len(lines[0])


def getEnergized(start, direction):
    energized = set()
    currents = []
    seenStates = set()
    directionDict = {"right": (0,1), "left": (0,-1), "down": (1,0), "up": (-1,0)}
    newPositions = set()

    if lines[start[0]][start[1]] == "/":
        if direction[0] == 1:
            direction = directionDict["left"]
        elif direction[0] == -1:
            direction = directionDict["right"]
        elif direction[1] == 1:
            direction = directionDict["up"]
        elif direction[1] == -1:
            direction = directionDict["down"]

    elif lines[start[0]][start[1]] == "\\":
        if direction[0] == 1:
            direction = directionDict["right"]
        elif direction[0] == -1:
            direction = directionDict["left"]
        elif direction[1] == 1:
            direction = directionDict["down"]
        elif direction[1] == -1:
            direction = directionDict["up"]

    elif lines[start[0]][start[1]] == "-":
        if direction[0] == 1:
            direction = directionDict["left"]
            newPositions.add((start, directionDict["right"]))
        elif direction[0] == -1:
            direction = directionDict["left"]
            newPositions.add((start, directionDict["right"]))

    elif lines[start[0]][start[1]] == "|":
        if direction[1] == 1:
            direction = directionDict["up"]
            newPositions.add((start, directionDict["down"]))
        elif direction[1] == -1:
            direction = directionDict["up"]
            newPositions.add((start, directionDict["down"]))

    currents.append([start, direction])

    while len(currents) > 0:

        current, direction = currents.pop(0)

        while inBounds(current) and (current, direction) not in seenStates:

            energized.add(current)
            seenStates.add((tuple(current),tuple(direction)))
            newPos = (current[0]+direction[0], current[1]+direction[1])

            if not inBounds(newPos):
                break

            newPositions = set()

            if lines[newPos[0]][newPos[1]] == "/":
                if direction[0] == 1:
                    direction = directionDict["left"]
                elif direction[0] == -1:
                    direction = directionDict["right"]
                elif direction[1] == 1:
                    direction = directionDict["up"]
                elif direction[1] == -1:
                    direction = directionDict["down"]

            elif lines[newPos[0]][newPos[1]] == "\\":
                if direction[0] == 1:
                    direction = directionDict["right"]
                elif direction[0] == -1:
                    direction = directionDict["left"]
                elif direction[1] == 1:
                    direction = directionDict["down"]
                elif direction[1] == -1:
                    direction = directionDict["up"]

            elif lines[newPos[0]][newPos[1]] == "-":
                if direction[0] == 1:
                    direction = directionDict["left"]
                    newPositions.add((newPos, directionDict["right"]))
                elif direction[0] == -1:
                    direction = directionDict["left"]
                    newPositions.add((newPos, directionDict["right"]))

            elif lines[newPos[0]][newPos[1]] == "|":
                if direction[1] == 1:
                    direction = directionDict["up"]
                    newPositions.add((newPos, directionDict["down"]))
                elif direction[1] == -1:
                    direction = directionDict["up"]
                    newPositions.add((newPos, directionDict["down"]))

            current = newPos
            for pos in newPositions:
                if pos not in currents:
                    currents.append(pos)

    return (len(energized))

print(f"Part 1: {getEnergized((0,0), (0,1))}")

energizedSet = set()
for row in range(len(lines)):
    for col in [0,len(lines[0])-1]:
        direction = (0,1) if col == 0 else (0,-1)
        start = (row,col)
        energizedSet.add(getEnergized(start, direction))
for col in range(len(lines[0])):
    for row in [0,len(lines)-1]:
        direction = (1,0) if row == 0 else (-1,0)
        start = (row,col)
        energizedSet.add(getEnergized(start, direction))

print(f"Part 2: {max(energizedSet)}")
