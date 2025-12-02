from pathlib import Path

def solve():

    from collections import defaultdict

    lines = Path(__file__).with_name('day_12_input.txt').open('r').read().strip().split("\n")

    def evaluate(value, registers):
        if value.isdigit():
            return int(value)
        return registers[value]
    
    def process(registers, lines):
        i = 0
        while i < len(lines):
            line = lines[i]
            if "cpy" in line:
                _, value, register = line.split(" ")
                registers[register] = evaluate(value, registers)
            elif "inc" in line:
                _, register = line.split(" ")
                registers[register] = registers[register] + 1
            elif "dec" in line:
                _, register = line.split(" ")
                registers[register] = registers[register] - 1
            elif "jnz" in line:
                _, value, jump = line.split(" ")
                if evaluate(value, registers) != 0:
                    i += int(jump) - 1
            i += 1
        return registers["a"]

    part1 = process(defaultdict(int), lines)
    part2_registers = defaultdict(int)
    part2_registers["c"] = 1
    part2 = process(part2_registers, lines)

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")