from pathlib import Path
lines = Path(__file__).with_name('day 15 input.txt').open('r').read().strip().split(",")

def hashFunction(string):
    val = 0
    for s in string:
        val += ord(s)
        val *= 17
        val %= 256
    return val

part1Score = 0
for line in lines:
    part1Score += hashFunction(line)

boxes = [[] for i in range(256)]

for line in lines:
    if "=" in line:
        exists = False
        label, num = line.split("=")
        num = int(num)
        box = hashFunction(label)
        for i in range(len(boxes[box])):
            if boxes[box][i][0] == label:
                boxes[box][i][1] = num
                exists = True
        if not exists:
            boxes[box].append([label, num])
    elif "-" in line:
        label = line.split("-")[0]
        box = hashFunction(label)
        for i in range(len(boxes[box])):
            if boxes[box][i][0] == label:
                boxes[box].pop(i)
                break

part2Score = 0
for box in range(len(boxes)):
    for lens in range(len(boxes[box])):
        part2Score += (box + 1)*(lens + 1)*(boxes[box][lens][1])

print(f"Part 1: {part1Score}\nPart 2: {part2Score}")