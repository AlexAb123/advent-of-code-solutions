from pathlib import Path
def solve():
    lines = [[l.split(" ") for l in line.replace(" | ", "|").split("|")] for line in Path(__file__).with_name('day_08_input.txt').open('r').read().strip().split("\n")]

    part1 = sum(len(s) in (2, 3, 4, 7) for line in lines for s in line[1])

    def find_assignments(signals):
        assignments = {}
        temp_assignments = {}
        for signal in filter(lambda signal: len(signal) in (2, 3, 4, 7), signals):
            if len(signal) == 2:
                temp_assignments[1] = set(signal)
                assignments[frozenset(signal)] = '1'
            elif len(signal) == 3:
                temp_assignments[7] = set(signal)
                assignments[frozenset(signal)] = '7'
            elif len(signal) == 4:
                temp_assignments[4] = set(signal)
                assignments[frozenset(signal)] = '4'
            elif len(signal) == 7:
                temp_assignments[8] = set(signal)
                assignments[frozenset(signal)] = '8'
        for signal in filter(lambda signal: len(signal) not in (2, 3, 4, 7), signals):
            if len(signal) == 5:
                if temp_assignments[1] <= set(signal):
                    temp_assignments[3] = set(signal)
                    assignments[frozenset(signal)] = '3'
                elif len(temp_assignments[4].intersection(set(signal))) == 3:
                    temp_assignments[5] = set(signal)
                    assignments[frozenset(signal)] = '5'
                else:
                    temp_assignments[2] = set(signal)
                    assignments[frozenset(signal)] = '2'
            elif len(signal) == 6:
                if temp_assignments[4] <= set(signal):
                    temp_assignments[9] = set(signal)
                    assignments[frozenset(signal)] = '9'
                elif temp_assignments[1] <= set(signal):
                    temp_assignments[0] = set(signal)
                    assignments[frozenset(signal)] = '0'
                else:
                    temp_assignments[6] = set(signal)
                    assignments[frozenset(signal)] = '6'

        return assignments
    
    part2 = 0
    for line in lines:
        num = ""
        assignments = find_assignments(line[0])
        for signal in line[1]:
            num += assignments[frozenset(signal)]
        part2 += int(num)
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")