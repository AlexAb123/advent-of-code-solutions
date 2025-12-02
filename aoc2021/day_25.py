from pathlib import Path


def solve():
    lines = Path(__file__).with_name("day_25_input.txt").open("r").read().strip().split("\n")

    east_cucumbers = set()
    south_cucumbers = set()

    rows = len(lines)
    cols = len(lines[0])
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] == ">":
                east_cucumbers.add((r, c))
            elif lines[r][c] == "v":
                south_cucumbers.add((r, c))


    def vis(rows, cols, east, south):

        grid = [["." for c in range(cols)] for r in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if (r, c) in east:
                    grid[r][c] = ">"
                elif (r, c) in south:
                    grid[r][c] = "v"
        for line in grid:
            print("".join(line))


    steps = 0
    moves = -1
    while moves != 0:

        steps += 1
        moves = 0

        new_east_cucumbers = set()

        for cucumber in east_cucumbers:
            next_cucumber = (cucumber[0] % rows, (cucumber[1] + 1) % cols)
            if next_cucumber not in east_cucumbers and next_cucumber not in south_cucumbers:
                new_east_cucumbers.add(next_cucumber)
                moves += 1
            else:
                new_east_cucumbers.add(cucumber)

        east_cucumbers = new_east_cucumbers

        new_south_cucumbers = set()

        for cucumber in south_cucumbers:
            next_cucumber = ((cucumber[0] + 1) % rows, cucumber[1] % cols)
            if next_cucumber not in east_cucumbers and next_cucumber not in south_cucumbers:
                new_south_cucumbers.add(next_cucumber)
                moves += 1
            else:
                new_south_cucumbers.add(cucumber)

        south_cucumbers = new_south_cucumbers

    return steps, "Day 25!"

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")