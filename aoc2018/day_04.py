from pathlib import Path

def solve():

    from collections import defaultdict
    lines = [line.split("]") for line in Path(__file__).with_name('day_04_input.txt').open('r').read().strip().split("\n")]

    """ def chronological(a):
        month = int(a[0].split("-")[1])
        day = int(a[0].split("-")[2].split(" ")[0])
        hour = int(a[0].split("-")[2].split(" ")[1].split(":")[0])
        minute = int(a[0].split("-")[2].split(" ")[1].split(":")[1])
        return ((month * 31 + day) * 24 + hour) * 60 + minute """
    # Already sorts it properly, dont need this function (although it does work for this input at least)
    lines.sort()

    guards = defaultdict(lambda: [0 for i in range(60)])
    current_guard = 0
    asleep = False
    fell_asleep = 0
    for line in lines:
        line[0] = line[0].replace("[", "").split()
        line[0][1] = int(line[0][1][3:5])
        current_minute = line[0][1]
        if "asleep" in line[1]:
            asleep = True
            fell_asleep = current_minute
        elif "wakes" in line[1]:
            asleep = False
            for i in range(fell_asleep, current_minute):
                guards[current_guard][i] += 1
        else:
            current_guard = int(line[1].split(" ")[2][1:])

    total_minutes = defaultdict(int)
    max_minutes = set()

    for guard in guards:
        total_minutes[guard] = sum(guards[guard])
        # guard, minute, freuqency
        max_minutes.add((guard, guards[guard].index(max(guards[guard])), max(guards[guard])))
    most_minutes = max(total_minutes.keys(), key=lambda x:total_minutes[x])
    part1 = most_minutes * guards[most_minutes].index(max(guards[most_minutes]))

    max_guard = max(max_minutes, key=lambda x: x[2])
    part2 = max_guard[0] * max_guard[1]

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")