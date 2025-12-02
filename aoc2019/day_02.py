from pathlib import Path
lines = list(map(int, Path(__file__).with_name('02_input.txt').open('r').read().strip().split(",")))

def getOutput(address1, address2, lines):
    lines[1] = address1
    lines[2] = address2
    for i in range(0, len(lines)-4, 4):
        if lines[i] == 1:
            lines[lines[i+3]] = lines[lines[i+1]] + lines[lines[i+2]]
        elif lines[i] == 2:
            lines[lines[i+3]] = lines[lines[i+1]] * lines[lines[i+2]]
        elif lines[i] == 99:
            break
    return lines[0]

print(f'Part 1: {getOutput(12, 2, lines.copy())}')

done = False
for i in range(100):
    if done:
        break
    for j in range(100):
        if getOutput(i, j, lines.copy()) == 19690720:
            print(f'Part 2: {i*100 + j}')
            done = True
            break