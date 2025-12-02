from pathlib import Path

def solve():

    line = Path(__file__).with_name('day_09_input.txt').open('r').read().strip()

    def decompressed_length(line, part2):

        total_length = 0

        while "(" in line:

            start = line.index("(")
            total_length += start
            line = line[start+1:]
            end = line.index(")")
            length, count = map(int, line[:end].split("x"))
            line = line[end+1:]
            if part2:
                total_length += decompressed_length(line[:length], part2) * count
            else:
                total_length += length * count
            line = line[length:]

        return total_length + len(line)
    
    part1 = decompressed_length(line, False)
    part2 = decompressed_length(line, True)

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")