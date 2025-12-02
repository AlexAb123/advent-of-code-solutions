from pathlib import Path

def solve():

    num = int(Path(__file__).with_name('day_17_input.txt').open('r').read().strip())

    buffer = [0]
    position = 0
    for i in range(1, 2018):
        position = (position + num) % i
        buffer.insert(position+1, i)
        position += 1
    part1 = buffer[position+1]
    position = 0
    part2 = 0
    for i in range(1, 50000001):
        position = (position + num) % i
        if position == 0:
            part2 = i
        position += 1
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")