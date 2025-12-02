from pathlib import Path

def solve():
        
    instructions = Path(__file__).with_name('day_12_input.txt').open('r').read().strip().split("\n")

    facing = 1j
    ship = 0
    for instruction in instructions:
        action = instruction[0]
        magnitude = int(instruction[1:])
        match action:
            case "F":
                ship += facing * magnitude
            case "N":
                ship += -1 * magnitude
            case "S":
                ship += 1 * magnitude
            case "E":
                ship += 1j * magnitude
            case "W":
                ship += -1j * magnitude
            case "R":
                facing *= (-1*1j) ** (magnitude//90)
            case "L":
                facing *= 1j ** (magnitude//90)
    part1 = int(abs(ship.real)+abs(ship.imag))

    ship = 0
    waypoint = -1 + 10j
    for instruction in instructions:
        action = instruction[0]
        magnitude = int(instruction[1:])
        match action:
            case "F":
                ship += waypoint * magnitude
            case "N":
                waypoint += -1 * magnitude
            case "S":
                waypoint += 1 * magnitude
            case "E":
                waypoint += 1j * magnitude
            case "W":
                waypoint += -1j * magnitude
            case "R":
                waypoint *= (-1*1j) ** (magnitude//90)
            case "L":
                waypoint *= 1j ** (magnitude//90)

    part2 = int(abs(ship.real)+abs(ship.imag))

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")