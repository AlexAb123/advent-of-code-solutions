print(f"Part 1: {sum(list((p := lambda c: 0 if all(d == 0 for d in c) else p([c[i] - c[i-1] for i in range(1, len(c))]) + c[-1])(l) for l in [list(map(int, i.split(" "))) for i in open('AOC2023/day 9 input.txt', 'r').read().strip().split("\n")]))}\nPart 2: {sum(list((p := lambda c: 0 if all(d == 0 for d in c) else p([c[i] - c[i-1] for i in range(1, len(c))]) + c[-1])(list(reversed(l))) for l in [list(map(int, i.split(" "))) for i in open('AOC2023/day 9 input.txt', 'r').read().strip().split("\n")]))}")

""" from pathlib import Path
lines = Path(__file__).with_name('day 9 input.txt').open('r').read().strip().split("\n")
lines = [list(map(int, line.split(" "))) for line in lines]

def extrapolate(line):
    if all(value == 0 for value in line):
        return 0
    else:
        return extrapolate([line[i+1] - line[i] for i in range(len(line)-1)]) + line[-1]

part1Score = sum([extrapolate(line) for line in lines])
part2Score = sum([extrapolate(list(reversed(line))) for line in lines])

print(f"Part 1: {part1Score}\nPart 2: {part2Score}") """