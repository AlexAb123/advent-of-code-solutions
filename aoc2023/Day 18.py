from pathlib import Path
from ast import literal_eval
lines = Path(__file__).with_name('day 18 input.txt').open('r').read().strip().split("\n")
lines = [line.split(" ") for line in lines]
lines = [[line[0], int(line[1]), line[2][2:-1]] for line in lines]

def shoelace(points):
    points.append(points[0])
    area = 0
    for i in range(len(points)-1):
        area += (points[i][0] * points[i+1][1]) - (points[i][1] * points[i+1][0])
    return int(area/2)

def getCornersAndPerimeter(part1):
    current = (0,0)
    corners = []
    perimeter = 0
    d1 = {"R": (0,1), "L": (0,-1), "D": (1,0), "U": (-1,0), "0": (0,1), "2": (0,-1), "1": (1,0), "3": (-1,0)}
    if part1:
        for line in lines:
            corners.append(current)
            d = d1[line[0]]
            new = (current[0] + d[0] * line[1], current[1] + d[1] * line[1])
            perimeter += abs(current[0] - new[0]) + abs(current[1] - new[1])
            current = new
    else:
        for _, _, line in lines:
            length = literal_eval("0x"+line[:-1])
            d = d1[line[-1]]
            corners.append(current)
            new = (current[0] + d[0] * length, current[1] + d[1] * length)
            perimeter += abs(current[0] - new[0]) + abs(current[1] - new[1])
            current = new

    return list(reversed([(corner[1], -1*corner[0])for corner in corners])), perimeter

corners, perimeter = getCornersAndPerimeter(True)
print(f"Part 1: {int(shoelace(corners) + perimeter/2 + 1)}")
corners, perimeter = getCornersAndPerimeter(False)
print(f"Part 2: {int(shoelace(corners) + perimeter/2 + 1)}")