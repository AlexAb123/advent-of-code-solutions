from pathlib import Path

def solve():

    row = list(Path(__file__).with_name('day_18_input.txt').open('r').read().strip())

    def next_row(row):
        new_row = []
        for r in range(len(row)):
            left = r-1 >= 0 and row[r-1] == "^"
            center = row[r] == "^"
            right = r+1 < len(row) and row[r+1] == "^"

            new_row.append("^" if (left and center and not right) or (right and center and not left) or (left and not center and not right) or (right and not center and not left) else ".")
        return new_row
    
    part1 = sum(tile == "." for tile in row)
    part2 = sum(tile == "." for tile in row)
    for i in range(399999):
        if i == 39:
            part1 = part2
        row = next_row(row)
        part2 += sum(tile == "." for tile in row)

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")