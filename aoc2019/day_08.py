from pathlib import Path
from collections import Counter
lines = Path(__file__).with_name('08_input.txt').open('r').read().strip()

layers = []
temp = []
width = 25
height = 6
for num in lines:
    temp.append(num)
    if len(temp) == (width*height):
        layers.append(temp)
        temp = []

counts = []
for layer in layers:
    counts.append(Counter(layer)["0"])
minimumZeroCounter = Counter(layers[counts.index(min(counts))])
print(f"Part 1: {minimumZeroCounter["1"] * minimumZeroCounter["2"]}")

newLayers = []
temp1 = []
temp2 = []
for i in range(len(layers)):
    temp1 = []
    for j in range(len(layers[i])):
        temp2.append(layers[i][j])
        if len(temp2) % width == 0:
            temp1.append(temp2)
            temp2 = []
    newLayers.append(temp1)
layers = newLayers

image = []
for i in range(height):
    temp = []
    for j in range(width):
        for layer in layers:
            if layer[i][j] == "1":
                temp.append(f'\u2588')
                break
            if layer[i][j] == "0":
                temp.append(' ')
                break
    image.append(temp)
print(f"Part 2:")
for i in image:
    print("".join(i))