from pathlib import Path
import re

def solve():

    def tokens_spent(machine, part2):
        a_x, a_y, b_x, b_y, p_x, p_y = machine
        if part2:
            p_x += 10000000000000
            p_y += 10000000000000

        a = (p_y*b_x-b_y*p_x)/(a_y*b_x-a_x*b_y)
        b = (p_y*a_x-a_y*p_x)/(b_y*a_x-b_x*a_y)

        if not part2 and (a > 100 or b > 100):
            return 0
        if a != int(a) or b != int(b):
            return 0
        return int(3*a + b)
    
    chunks = Path(__file__).with_name('day_13_input.txt').open('r').read().strip().split("\n\n")
    machines = [list(map(int, re.findall(r"\d+", chunk))) for chunk in chunks]
    part1 = sum(tokens_spent(machine, False) for machine in machines)
    part2 = sum(tokens_spent(machine, True) for machine in machines)
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")