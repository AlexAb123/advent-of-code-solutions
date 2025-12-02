from pathlib import Path
lines = Path(__file__).with_name('day_08_input.txt').open('r').read().strip().split("\n")
lines = [line.split(" ") for line in lines]


nops = []
jmps = []
accs = []
for i, line in enumerate(lines):
    if line[0] == "jmp":
        jmps.append(i)
    elif line[0] == "nop":
        nops.append(i)
    else:
        accs.append(i)

def isTerminatingAndAccumulator(nops, jmps, accs):
    doneInstructions = set()
    current = 0
    accumulator = 0
    while current not in doneInstructions:
        if current == len(lines):
            return (True, accumulator)
        doneInstructions.add(current)

        if current in accs:
            if lines[current][1][0] == "+":
                accumulator += int(lines[current][1][1:])
            else:
                accumulator -= int(lines[current][1][1:])
            current += 1

        elif current in jmps:
            if lines[current][1][0] == "+":
                current += int(lines[current][1][1:])
            else:
                current -= int(lines[current][1][1:])
        else:
            current += 1
    return (False, accumulator)

print(f"Part 1: {isTerminatingAndAccumulator(nops, jmps, accs)[1]}")

for j in jmps:
    newJmps = jmps.copy()
    newNops = nops.copy()
    newJmps.remove(j)
    newNops.append(j)
    value = isTerminatingAndAccumulator(newNops, newJmps, accs)
    if value[0]:
        print(f"Part 2: {value[1]}")
        break
for n in nops:
    newNops = nops.copy()
    newJmps = jmps.copy()
    newNops.remove(n)
    newJmps.append(n)
    value = isTerminatingAndAccumulator(newNops, newJmps, accs)
    if value[0]:
        print(f"Part 2: {value[1]}")
        break