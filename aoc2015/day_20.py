from pathlib import Path

def solve():

    target_presents = int(Path(__file__).with_name('day_20_input.txt').open('r').read().strip())

    def get_divisors(num):
        divisors = set()
        for i in range(1, int(num**0.5)+1):
            if num % i == 0:
                divisors.add(i)
                divisors.add(num//i)
        return divisors
    
    def get_presents1(house):
        presents = 0
        for divisor in get_divisors(house):
            presents += divisor * 10
        return presents
    
    def get_presents2(house):
        presents = 0
        for divisor in get_divisors(house):
            if house // divisor > 50:
                continue
            presents += divisor * 11
        return presents
    
    house = 1
    while get_presents1(house) < target_presents:
        house += 1
    part1 = house

    house = 1
    while get_presents2(house) < target_presents:
        house += 1
    part2 = house

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")