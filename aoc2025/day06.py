from math import prod

def solve(data):

    *lines, ops = data.split("\n")
    lines[0] += " "

    part1 = part2 = 0
    indices = [i for i, op in enumerate(ops) if op != " "] + [len(lines[0])]
    for i in range(len(indices) - 1):
        nums = [line[indices[i]:indices[i+1] - 1] for line in lines]
        f = sum if ops[indices[i]] == "+" else prod
        part1 += f(int(n.strip()) for n in nums)
        part2 += f(int("".join(n).strip()) for n in zip(*nums))

    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    data = (Path(__file__).parent/"inputs"/"day06.txt").read_text().strip()
    start = time()
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")
