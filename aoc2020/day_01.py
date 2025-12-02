from pathlib import Path
lines = list(map(int, Path(__file__).with_name('day_01_input.txt').open('r').read().strip().split("\n")))

def part1(lines):
    for num1 in lines:
        for num2 in lines:
            if num1 != num2 and num1 + num2 == 2020:
                return num1*num2
def part2(lines):
    for num1 in lines:
        for num2 in lines:
            for num3 in lines:
                if sum((num1, num2, num3)) == 2020:
                    return num1*num2*num3
print(f"Part 1: {part1(lines)}")
print(f"Part 2: {part2(lines)}")