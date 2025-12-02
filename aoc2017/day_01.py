from pathlib import Path

def solve():
    line = [int(c) for c in Path(__file__).with_name('day_01_input.txt').open('r').read().strip()]
    part1 = sum(map(lambda i: line[i] if line[i] == line[(i+1) % len(line)] else 0, range(len(line))))
    part2 = sum(map(lambda i: line[i] if line[i] == line[(i+len(line)//2) % len(line)] else 0, range(len(line))))
    return part1, part2
""" part1 = 0
part2 = 0
for i in range(len(line)):
    if line[i] == line[(i+1) % len(line)]:
        part1 += line[i]
    if line[i] == line[(i+len(line)//2) % len(line)]:
        part2 += line[i]
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
 """
if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")