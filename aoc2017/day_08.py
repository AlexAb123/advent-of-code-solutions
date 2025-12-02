from pathlib import Path

def solve():

    from collections import defaultdict

    lines = Path(__file__).with_name('day_08_input.txt').open('r').read().strip().split("\n")

    part2 = 0
    registers = defaultdict(int)

    for line in lines:
        line = line.split(" ")
        register = line[0]
        sign = 1 if line[1] == "inc" else -1
        value = int(line[2])
        cond_register = line[4]
        cond = line[5]
        cond_value = int(line[6])

        match cond:
            case ">":
                if not registers[cond_register] > cond_value:
                    continue
            case "<":
                if not registers[cond_register] < cond_value:
                    continue
            case ">=":
                if not registers[cond_register] >= cond_value:
                    continue
            case "<=":
                if not registers[cond_register] <= cond_value:
                    continue
            case "==":
                if not registers[cond_register] == cond_value:
                    continue
            case "!=":
                if not registers[cond_register] != cond_value:
                    continue
        registers[register] += sign * value
        part2 = max(part2, registers[register])

    part1 = max(registers.values())

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")