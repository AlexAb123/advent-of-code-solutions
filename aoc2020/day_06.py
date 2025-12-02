from pathlib import Path
from collections import defaultdict
lines = Path(__file__).with_name('day_06_input.txt').open('r').read().strip().split("\n\n")
part1Lines = [line.replace("\n", "") for line in lines]

answers = []
for line in part1Lines:
    yes = set()
    for question in line:
        yes.add(question)
    answers.append(len(yes))
print(f"Part 1: {sum(answers)}")

allYes = 0
part2Lines = [line.split("\n") for line in lines]
for line in part2Lines:
    answers = defaultdict(int)
    for person in line:
        for question in person:
            answers[question] += 1
    for value in answers.values():
        if value == len(line):
            allYes += 1
print(f"Part 2: {allYes}")