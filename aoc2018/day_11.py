from pathlib import Path

def solve():

    serial = int(Path(__file__).with_name('day_11_input.txt').open('r').read().strip())

    fuel_cell = {}
    for r in range(1, 301):
        for c in range(1, 301):
            rack = c + 10
            power = rack * r
            power += serial
            power *= rack
            power = (power // 100) % 10
            power -= 5
            fuel_cell[(r, c)] = power

    def total_power_level(row, col, size):
        total_power = 0
        for r in range(row, row + size):
            for c in range(col, col + size):
                total_power += fuel_cell[(r, c)]
        return total_power

        print(row, col, size)
        if (row, col, size) in cache:
            return cache[(row, col, size)]
        if size == 1:
            cache[(row, col, size)] = fuel_cell[row, col]
            return cache[(row, col, size)]
        
        total_power = 0
        for r in range(1, row + size - 1):
            total_power += fuel_cell[r, col]
        for c in range(1, col + size - 1):
            total_power += fuel_cell[row, c]


        total_power += total_power_level(row, col, size - 1)
        cache[(row, col, size)] = total_power
        return cache[(row, col, size)]

    max_power = 0
    for r in range(1, 301 - 3):
        for c in range(1, 301 - 3):
            if (power := total_power_level(r, c, 3)) > max_power:
                max_power = power
                part1 = f"{c},{r}"

    max_power = 0
    part2 = 0
    for size in range(1, 300):
        for r in range(1, 301 - size):
            for c in range(1, 301 - size):
                if (power := total_power_level(r, c, size)) > max_power:
                    max_power = power
                    part2 = f"{c},{r},{size}"

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")