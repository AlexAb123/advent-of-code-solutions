from pathlib import Path
positions = list(map(int, Path(__file__).with_name('day_07_input.txt').open('r').read().strip().split(",")))

def solve():
    fuel_costs1 = set()
    fuel_costs2 = set()
    for i in range(max(positions)+1):
        fuel_costs1.add(sum([abs(x-i) for x in positions]))
        fuel_costs2.add(sum([abs(x-i)*(abs(x-i)+1)//2 for x in positions]))
    return min(fuel_costs1), min(fuel_costs2)
if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")