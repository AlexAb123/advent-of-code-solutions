from pathlib import Path

def solve():
        
    banks = list(map(int, Path(__file__).with_name('day_06_input.txt').open('r').read().strip().split("\t")))

    def redistribute_blocks(banks):
        max_bank = banks.index(max(banks))
        blocks_left = banks[max_bank]
        banks[max_bank] = 0
        i = (max_bank + 1) % len(banks)
        while blocks_left > 0:
            banks[i] += 1
            blocks_left -=1
            i = (i + 1) % len(banks)
        return banks

    seen_states = set()
    i = 0
    while tuple(banks) not in seen_states:
        seen_states.add(tuple(banks))
        banks = redistribute_blocks(banks)
        i += 1
    part1 = i
    i = 0
    while tuple(banks) not in seen_states:
        seen_states.add(tuple(banks))
        banks = redistribute_blocks(banks)
        i += 1
    part2 = i
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")