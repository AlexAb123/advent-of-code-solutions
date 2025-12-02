from pathlib import Path

def solve():
    lines = Path(__file__).with_name('day_11_input.txt').open('r').read().strip().split("\n")
    grid = {r+c*1j: int(lines[r][c]) for c in range(len(lines[0])) for r in range(len(lines))}
    offsets = {-1-1j, -1, -1+1j, -1j, 1j, 1-1j, 1, 1+1j}
    class Octopus:
        def __init__(self, energy_level):
            self.energy_level = energy_level
            self.adjacents: set[Octopus] = set()
            self.flashes = 0
            self.flashed = False

        def flash(self):
            self.flashes += 1
            self.flashed = True
            for octopus in self.adjacents:
                octopus.energy_level += 1
                if not octopus.flashed and octopus.energy_level > 9:
                    octopus.flash()

        def __repr__(self):
            return f"Energy Level: {self.energy_level}, Flashes: {self.flashes}"

    octopi: set[Octopus] = set()
    octopi_grid = {}
    # Create octopi
    for pos in grid:
        new_octopus = Octopus(grid[pos])
        octopi_grid[pos] = new_octopus
        octopi.add(new_octopus)

    # Initialize adjacents
    for pos in octopi_grid:
        adjacents = set()
        for adj in (pos + d for d in offsets):
            if adj in octopi_grid:
                adjacents.add(octopi_grid[adj])
        octopi_grid[pos].adjacents = adjacents

    step = 0
    while sum(octopus.flashed for octopus in octopi) != len(octopi) or step < 100:

        step += 1

        for octopus in octopi:
            if octopus.flashed:
                octopus.flashed = False
                octopus.energy_level = 0
                
        for octopus in octopi:
            octopus.energy_level += 1

        for octopus in octopi:
            if not octopus.flashed and octopus.energy_level > 9:
                octopus.flash()
        if step == 100:
            part1 = sum(octopus.flashes for octopus in octopi)
    part2 = step

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")

# Alternative solution without using classes. Slower to run
def solve():

    lines = Path(__file__).with_name('day_11_input.txt').open('r').read().strip().split("\n")

    grid = {r+c*1j: int(lines[r][c]) for c in range(len(lines[0])) for r in range(len(lines))}

    offsets = {-1-1j, -1, -1+1j, -1j, 1j, 1-1j, 1, 1+1j}
    def flash(pos, flashed):

        if pos in flashed:
            return 0
        
        flashes = 1
        flashed.add(pos)

        for adj in (pos + d for d in offsets):

            if adj not in grid:
                continue

            grid[adj] += 1

            if grid[adj] > 9:
                flashes += flash(adj, flashed)

        return flashes

    flashes = 0
    flashed = set()
    step = 0
    while len(flashed) != len(grid) or step < 100:

        step += 1
        flashed = set()

        for pos in grid:
            grid[pos] += 1

        for pos in grid:
            if pos not in flashed and grid[pos] > 9:
                flashes += flash(pos, flashed)

        for pos in flashed:
            grid[pos] = 0
        
        if step == 100:
            part1 = flashes

    part2 = step
    return part1, part2