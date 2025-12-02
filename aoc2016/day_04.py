from pathlib import Path

def solve():
        
    from collections import Counter
    lines = [["".join(line.split("-")[:-1])] + line.split("-")[-1].replace("]", "").split("[") for line in Path(__file__).with_name('day_04_input.txt').open('r').read().strip().split("\n")]

    def shift(letter, shift):
        letters = "abcdefghijklmnopqrstuvwxyz"
        return letters[(letters.index(letter) + shift) % len(letters)]

    part1 = 0
    for line in lines:
        counter = Counter(line[0])
        most_common = "".join(sorted(list(counter.keys()), key=lambda x: (-1*counter[x], x)))[0:5]
        
        if most_common == line[2]:
            part1 += int(line[1])
        name = ""
        for letter in line[0]:
            name += shift(letter, int(line[1]))
        if name == "northpoleobjectstorage":
            part2 = int(line[1])

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")