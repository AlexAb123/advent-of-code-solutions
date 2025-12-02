from pathlib import Path
lines = [list(map(int, value.split("x"))) for value in Path(__file__).with_name('day_02_input.txt').open('r').read().strip().split("\n")]

part1 = 0
part2 = 0
for box in lines:
    part1 += 2 * box[0] * box[1]
    part1 += 2 * box[1] * box[2]
    part1 += 2 * box[0] * box[2]
    part2 += box[0] * box[1] * box[2]
    box.remove(max(box))
    part1 += box[0] * box[1]
    part2 += 2 * box[0] + 2 * box[1]
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
