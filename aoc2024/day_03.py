from pathlib import Path

def solve():
    
    import re

    line = Path(__file__).with_name('day_03_input.txt').open('r').read().strip()
    commands = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)
    part1 = 0
    part2 = 0
    enabled = True

    for command in commands:

        if command == "do()":
            enabled = True
            
        elif command == "don't()":
            enabled = False

        else:
            num1, num2 = map(int, command[4:-1].split(","))
            part1 += num1 * num2

            if enabled:
                part2 += num1 * num2

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")