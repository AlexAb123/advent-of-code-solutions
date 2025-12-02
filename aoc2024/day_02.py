from pathlib import Path

def solve():

    lines = [list(map(int, line.split())) for line in Path(__file__).with_name('day_02_input.txt').open('r').read().strip().split("\n")]
    
    def safe(report):
        differences = [report[i+1] - report[i] for i in range(len(report)-1)]
        increasing_or_decreasing = report == sorted(report) or report == sorted(report, reverse=True)
        return increasing_or_decreasing and all(1 <= abs(d) <= 3 for d in differences)
    
    part1 = 0
    part2 = 0

    for report in lines:

        if safe(report):
            part1 += 1
            part2 += 1
            continue

        if any(safe(new_report) for new_report in [report[:i] + report[i+1:] for i in range(len(report))]):
            part2 += 1
            continue
        
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")