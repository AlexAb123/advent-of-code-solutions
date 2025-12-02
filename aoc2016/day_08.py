from pathlib import Path

def solve():

    import re

    lines = Path(__file__).with_name('day_08_input.txt').open('r').read().strip().split("\n")

    part1 = 0
    part2 = 0

    rows = 6
    cols = 50

    pixels = set()

    for line in lines:
        if "rect" in line:
            col, row = map(int, re.findall(r"(\d+)x(\d+)", line)[0])
            for r in range(row):
                for c in range(col):
                    pixels.add(r + c * 1j)
        elif "rotate" in line:
            remove = set()
            add = set()
            if "row" in line:
                row, d = map(int, line.split("=")[-1].split(" ")[::2])
                for pixel in pixels:
                    if int(pixel.real) == row:
                        remove.add(pixel)
                        add.add(pixel.real + ((d + pixel.imag) % cols) * 1j)
            elif "column" in line:
                col, d = map(int, line.split("=")[-1].split(" ")[::2])
                for pixel in pixels:
                    if int(pixel.imag) == col:
                        remove.add(pixel)
                        add.add((pixel.real + d) % rows + pixel.imag * 1j)
            pixels.difference_update(remove)
            pixels.update(add)

    part1 = len(pixels)
    part2 = "\n"
    grid = [[" " for _ in range(cols)] for _ in range(rows)]
    for pixel in pixels:
        grid[int(pixel.real)][int(pixel.imag)] = '\u2588'
    for line in grid:
        part2 += "".join(line) + "\n"

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")