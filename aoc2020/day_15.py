from pathlib import Path

def solve():

    from collections import defaultdict
    numbers = list(map(int, Path(__file__).with_name('day_15_input.txt').open('r').read().strip().split(",")))

    def simulate_game(max_turns):
        previous = 0
        last_spoken = defaultdict(list)
        for i in range(max_turns):

            if i < len(numbers):
                previous = numbers[i]

            elif len(last_spoken[previous]) == 1:
                previous = 0

            else:
                previous = last_spoken[previous][-1] - last_spoken[previous][-2]

            last_spoken[previous].append(i)
            
        return previous

    part1 = simulate_game(2020)
    part2 = simulate_game(30000000)

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")