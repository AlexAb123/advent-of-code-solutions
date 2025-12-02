from pathlib import Path

def solve():

    def process(data):
        return data + [0] + list(map(lambda n: int(not n), reversed(data.copy())))

    data = list(map(int, Path(__file__).with_name('day_16_input.txt').open('r').read().strip()))
    while len(data) < 272:
        data = process(data)
    data = data[:272]
    while len(data) % 2 == 0:
        new_data = []
        for i in range(0, len(data), 2):
            new_data.append(int(data[i] == data[i+1]))
        data = new_data
    part1 = "".join(map(str, data))
    data = list(map(int, Path(__file__).with_name('day_16_input.txt').open('r').read().strip()))

    while len(data) < 35651584:
        data = process(data)
    data = data[:35651584]
    while len(data) % 2 == 0:
        new_data = []
        for i in range(0, len(data), 2):
            new_data.append(int(data[i] == data[i+1]))
        data = new_data
    part2 = "".join(map(str, data))
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")