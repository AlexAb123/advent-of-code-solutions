from pathlib import Path

def solve():

    from collections import defaultdict

    lines = Path(__file__).with_name('day_25_input.txt').open('r').read().strip().split("\n")

    def evaluate(value, registers):
        if value.replace("-", "").isdigit():
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
                    i += evaluate(jump, registers) - 1

            elif "out" in line:
                _, value = line.split(" ")
                yield evaluate(value, registers)

            i += 1

        return registers["a"]

    part1 = 1
    while True:
        outputs = []
        found = False
        for output in process(defaultdict(int, {"a": part1}), lines):
            outputs.append(output)
            if outputs[0] != 0:
                break
            elif len(outputs) == 25: # Arbitrarily choose 25. Works for my input. Doubt it doesn't work for any others
                if outputs == [n % 2 for n in range(25)]:
                    found = True
                    break
                else:
                    break
        if found:
            break
        part1 += 1

    part2 = "Day 25!"
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")