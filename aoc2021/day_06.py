from pathlib import Path
lanternFish = list(map(int, Path(__file__).with_name('day_06_input.txt').open('r').read().strip().split(",")))

def solve():
    fish = [0,0,0,0,0,0,0,0,0]

    for daysLeft in lanternFish:
        fish[daysLeft] += 1
        
    for day in range(256):
        zero = fish[0]
        fish[0] = fish[1]
        fish[1] = fish[2]
        fish[2] = fish[3]
        fish[3] = fish[4]
        fish[4] = fish[5]
        fish[5] = fish[6]
        fish[6] = fish[7] + zero
        fish[7] = fish[8]
        fish[8] = zero

        if day == 79:
            part1 = sum(fish)

    part2 = sum(fish)
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")