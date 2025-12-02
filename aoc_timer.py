import importlib
from os import sep
from pathlib import Path
from time import time

total_time = 0
total_days = 0
year = input("Enter Year:\n")
days = int(input("Enter number of days:\n"))
print()

for day in (map(str, range(1, days + 1))):

    if len(day) == 1:
        day = "0" + day
        
    # Import each file and measure time taken
    try:
        module = importlib.import_module(f"aoc{year}.day{day}")
        start = time()
        part1, part2 = module.solve(Path(f"aoc{year}{sep}inputs{sep}day{day}.txt"))
        end = time()
        total_time += end - start
        print(f"day{day}: Part 1: {part1:<15} Part 2: {part2:<15} {(end - start)*1000:.2f} ms")
        total_days += 1

    except ModuleNotFoundError:
        print(f"day{day}.py not found")

    except AttributeError:
        print(f"day{day}.py does not have function 'solve'")
        
print(f"Total time taken for {f"{total_days} days" if total_days != 1 else "1 day"}: {total_time*1000:.2f} ms")
