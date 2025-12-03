def solve(input_path):

    batteries = input_path.open('r').read().strip().split("\n")

    def joltage(battery, num_remove):
        window_size = num_remove + 1
        if num_remove == 0:
            return battery
        if len(battery) == num_remove:
            return ""
        window = battery[:window_size]
        max_index = window.index(str(max(map(int, list(window)))))
        return battery[max_index] + joltage(battery[max_index + 1:], num_remove - max_index)
    
    part1 = sum(int(joltage(battery, len(battery) - 2)) for battery in batteries)
    part2 = sum(int(joltage(battery, len(battery) - 12)) for battery in batteries)

    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    start = time()
    part1, part2 = solve(Path(__file__).parent/"inputs"/"day03.txt")
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")