from pathlib import Path

def solve():
    
    import re
    chunks = Path(__file__).with_name('day_13_input.txt').open('r').read().strip().split("\n\n")
    positions = chunks[0].split("\n")
    folds = chunks[1].split("\n")

    dots = set()
    for pos in positions:
        col, row = map(int, pos.split(","))
        dots.add((row, col))

    for i, fold in enumerate(folds):
        fold_line = int(re.search(r"\d+", fold)[0])
        new_dots = dots.copy()
        for dot in dots:

            if "y" in fold:

                if dot[0] > fold_line:
                    new_dots.remove(dot)
                    new_dots.add((2*fold_line-dot[0], dot[1]))

            else:

                if dot[1] > fold_line:
                    new_dots.remove(dot)
                    new_dots.add((dot[0], 2*fold_line-dot[1]))

        dots = new_dots
        if i == 0:
            part1 = len(dots)

    max_row = max(map(lambda dot: dot[0], dots))
    max_col = max(map(lambda dot: dot[1], dots))

    part2 = "\n" + "\n".join("".join(line) for line in [["\u2588" if (r,c) in dots else " " for c in range(max_col+1)] for r in range(max_row+1)])

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")