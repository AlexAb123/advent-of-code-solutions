from pathlib import Path
lines = list(map(int, Path(__file__).with_name('day_09_input.txt').open('r').read().strip().split("\n")))

def isSum(target, prev25):
    for i, n1 in enumerate(prev25):
        for j, n2 in enumerate(prev25):
            if i != j and n1+n2 == target:
                return True
    return False

preambleLength = 25
for i in range(preambleLength, len(lines)):
    if not isSum(lines[i], lines[i-preambleLength:i]):
        brokenNumber = lines[i]
        break
print(f"Part 1: {brokenNumber}")

done = False
for length in range(2, len(lines)):
    if done:
        break
    for start in range(len(lines)):
        if sum(lines[start:start+length]) == brokenNumber:
            part2Score = min(lines[start:start+length]) + max(lines[start:start+length])
            done = True
            break
print(f"Part 1: {part2Score}")
