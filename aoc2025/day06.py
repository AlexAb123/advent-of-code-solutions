from math import prod

def solve(data):

    *lines, ops = data.split("\n")
    lines = [line + " " for line in lines]

    part1 = part2 = 0
    
    indices = [i for i, op in enumerate(ops) if op != " "] + [len(lines[0])]

    for i in range(len(indices) - 1):
        start = indices[i]
        end = indices[i+1] - 1

        nums = [list(line[start:end]) for line in lines]

        nums1 = [int("".join(n).strip()) for n in nums]
        nums2 = [int("".join(n).strip()) for n in zip(*nums)]

        f = sum if ops[start] == "+" else prod
        part1 += f(nums1)
        part2 += f(nums2)

    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    start = time()
    part1, part2 = solve((Path(__file__).parent/"inputs"/"day06.txt").read_text().strip())
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")