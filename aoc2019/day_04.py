from pathlib import Path
lines = list(map(int, Path(__file__).with_name('04_input.txt').open('r').read().strip().split("-")))

def isNotDecreasing(password):
    for i in range(len(password)-1):
        if int(password[i]) > int(password[i+1]):
            return False
    return True

def hasDoublePart1(password):
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            return True
    return False

def hasDoublePart2(password):
    for i in range(len(password)-1):
        if i == 0:
            if password[i] == password[i+1] and password[i+2] != password[i]:
                return True
        elif 1 <= i < len(password)-2:
            if password[i] == password[i+1] and password[i+2] != password[i] and password[i-1] != password[i]:
                return True
        elif i >= len(password)-2:
            if password[i] == password[i+1] and password and password[i-1] != password[i]:
                return True
    return False

part1Score = 0
part2Score = 0
for password in range(lines[0], lines[1]+1):
    if isNotDecreasing(str(password)) and hasDoublePart1(str(password)):
        part1Score += 1
    if isNotDecreasing(str(password)) and hasDoublePart2(str(password)):
        part2Score += 1
print(f'Part 1: {part1Score}')
print(f'Part 2: {part2Score}')