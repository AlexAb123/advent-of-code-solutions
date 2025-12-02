from pathlib import Path

def solve():

    import re

    lines = Path(__file__).with_name('day_20_input.txt').open('r').read().strip().split("\n")

    part2 = 0

    particles = []
    for line in lines:
        nums = tuple(map(int, re.findall(r'-?\d+', line)))
        particles.append((nums[0:3], nums[3:6], nums[6:]))

    def magnitude(vec):
        return sum(v * v for v in vec) ** 0.5

    part1 = particles.index(min(particles, key=lambda particle: [magnitude(particle[i]) for i in range(2, -1 , -1)]))
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")