def solve(data):

    banks = data.split("\n")

    def joltage(bank, num_remove):
        window_size = num_remove + 1
        if num_remove == 0:
            return bank
        if len(bank) == num_remove:
            return ""
        window = bank[:window_size]
        max_index = window.index(str(max(map(int, list(window)))))
        return bank[max_index] + joltage(bank[max_index + 1:], num_remove - max_index)
    
    part1 = sum(int(joltage(bank, len(bank) - 2)) for bank in banks)
    part2 = sum(int(joltage(bank, len(bank) - 12)) for bank in banks)

    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    data = (Path(__file__).parent/"inputs"/"day03.txt").read_text().strip()
    start = time()
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")