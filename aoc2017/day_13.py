from pathlib import Path

def solve():

    layers = [line.split(": ") for line in Path(__file__).with_name('day_13_input.txt').open('r').read().strip().split("\n")]
    layers = {int(layer[0]): int(layer[1]) for layer in layers}

    part1 = 0
    for packet_depth in range(min(layers), max(layers)+1):
        if packet_depth in layers and packet_depth % ((2 * layers[packet_depth]) - 2) == 0:
            part1 += packet_depth * layers[packet_depth]
    part2 = 0

    delay = 0
    caught = True
    while caught:
        caught = False
        for packet_depth in range(min(layers), max(layers)+1):
            if packet_depth in layers and (delay + packet_depth) % ((2 * layers[packet_depth]) - 2) == 0:
                caught = True
                delay += 1
                break

    part2 = delay

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")