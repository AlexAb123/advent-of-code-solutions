from pathlib import Path

def solve():

    from collections import defaultdict

    lines = Path(__file__).with_name('day_23_input.txt').open('r').read().strip().split("\n")

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
                if not register.replace("-", "").isdigit():
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

            elif "tgl" in line:
                print(registers)
                _, register = line.split("tgl ")
                if not (0 <= i + registers[register] < len(lines)):
                    pass
                elif "inc" in lines[i + registers[register]]:
                    lines[i + registers[register]] = lines[i + registers[register]].replace("inc", "dec")
                elif "dec" in lines[i + registers[register]]:
                    lines[i + registers[register]] = lines[i + registers[register]].replace("dec", "inc")
                elif "tgl" in lines[i + registers[register]]:
                    lines[i + registers[register]] = lines[i + registers[register]].replace("tgl", "inc")
                elif "cpy" in lines[i + registers[register]]:
                    lines[i + registers[register]] = lines[i + registers[register]].replace("cpy", "jnz")
                elif "jnz" in lines[i + registers[register]]:
                    lines[i + registers[register]] = lines[i + registers[register]].replace("jnz", "cpy")
            i += 1

        return registers["a"]

    part1 = process(defaultdict(int, {"a": 7}), lines.copy())
    part2 = process(defaultdict(int, {'a': 12}), lines.copy())
    """     
    Can optimize by replacing this addition loop with a multiply:
    cpy b c
    inc a
    dec c
    jnz c NUM
    dec d
    jnz d NUM 
    """

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")