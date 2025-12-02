from pathlib import Path

def solve():
    from heapq import heappush, heappop

    line = Path(__file__).with_name('day_09_input.txt').open('r').read().strip()

    idx, files1, files2, spaces = 0, [], [], [[] for _ in range(10)]
    for i, val in enumerate(line):
        val = int(val)
        if i % 2 == 0:
            files1 += [i//2] * val if i%2 == 0 else ["."] * val
            files2.append([idx, val, i//2])
        else:
            files1 += ["."] * val
            spaces[val].append([idx, val])
        idx += val

    i = 0
    while i < len(files1):
        if files1[i] == ".":
            while files1[-1] == ".":
                files1.pop(-1)
            files1[i] = files1.pop(-1)
        else:
            i += 1
    part1 = sum(files1[i]*i if files1[i] != "." else 0 for i in range(len(files1)))

    compacted_files = []
    for file in reversed(files2):

        valid_spaces = [spaces[j][0] for j in range(file[1], len(spaces)) if spaces[j][0][0] < file[0]]
        if not valid_spaces:
            compacted_files.append(file)
            continue
        space = min(valid_spaces)

        heappop(spaces[space[1]])
        # If there will be remaining space in this chunk, add it
        if space[1] - file[1] > 0:
            heappush(spaces[space[1] - file[1]], [space[0] + file[1], space[1] - file[1]])

        # Add the file at the index where the space was
        compacted_files.append([space[0], file[1], file[2]])

    part2 = sum((file[2] * file[1] * (2*file[0] + file[1] - 1))//2 for file in compacted_files)

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")