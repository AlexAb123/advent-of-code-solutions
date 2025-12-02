from pathlib import Path

def solve():

    from collections import defaultdict
    import re

    lines = Path(__file__).with_name('day_10_input.txt').open('r').read().strip().split("\n")

    commands = {}

    bots = defaultdict(set)
    for line in lines:
        if "value" not in line:
            bot, lo, hi = map(int, re.findall(r"\d+", line))
            commands[bot] = ((lo, line.split(" ")[5] == "output"), (hi, line.split(" ")[-2] == "output"))
        else:
            value, bot = map(int, re.findall(r"\d+", line))
            bots[bot].add(value)
            
    q = []
    for bot in bots.keys():
        if len(bots[bot]) == 2: # If bot starts with two values add it to the queue
            q.append(bot)

    outputs = {}
    while q: # Topological Sort
        bot = q.pop(0)
        command = commands[bot]

        if bots[bot] == {61, 17}:
            part1 = bot

        for value, target, output in (min(bots[bot]), *command[0]), (max(bots[bot]), *command[1]):

            if not output: # If bot gives lo to another bot
                bots[target].add(value)
                if len(bots[target]) == 2:
                    q.append(target)
            else: # If bot lo gives to output channel
                outputs[target] = value

            bots[bot].remove(value)

    part2 = outputs[0] * outputs[1] * outputs[2]

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")