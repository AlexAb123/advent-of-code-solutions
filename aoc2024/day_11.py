from pathlib import Path

def solve():
    cache = {}
    def count_stones(stone, blinks_left):
        if (stone, blinks_left) in cache:
            return cache[(stone, blinks_left)]
        elif blinks_left == 0:
            result = 1
            return 1
        elif stone == 0:
            result = count_stones(1, blinks_left-1)
        elif (num_digits := len(str(stone))) % 2 == 0:
            result = count_stones(stone // (10**(num_digits//2)), blinks_left-1) + count_stones(stone % (10**(num_digits//2)), blinks_left-1)
        else:
            result = count_stones(2024 * stone, blinks_left-1)
        cache[(stone, blinks_left)] = result
        return result

    line = list(map(int, Path(__file__).with_name('day_11_input.txt').open('r').read().strip().split(" ")))

    return sum((count_stones(stone, 25)) for stone in line), sum((count_stones(stone, 75)) for stone in line)

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")