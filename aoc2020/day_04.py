from pathlib import Path
import re
passports = Path(__file__).with_name('day_04_input.txt').open('r').read().strip().split("\n\n")
passports = [passport.replace("\n", " ").split(" ") for passport in passports]

fieldsOrdering = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
passports = [[field.split(":") for field in passport] for passport in passports]
passports = [sorted(field, key=lambda x: fieldsOrdering.index(x[0])) for field in passports]

def isValidPart1(passport):
    passportString = ""
    for field in passport:
        passportString += field[0]
    for field in fields:
        if field not in passportString:
            return False
    return True

eyeColor = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
def isValidHairColor(string):
    valid = '0123456789abcdef'
    for s in string:
        if s not in valid:
            return False
    return True

def isValidPart2(passport):
    if not isValidPart1(passport):
        return False
    if not (1920 <= int(passport[0][1]) <= 2002):
        return False
    if not (2010 <= int(passport[1][1]) <= 2020):
        return False
    if not (2020 <= int(passport[2][1]) <= 2030):
        return False
    if not (("cm" in passport[3][1] and 150 <= int(passport[3][1].replace("cm", "")) <= 193) or ("in" in passport[3][1] and 59 <= int(passport[3][1].replace("in", "")) <= 76)):
        return False
    if not (passport[4][1][0] == "#" and isValidHairColor(passport[4][1][1:])):
        return False
    if not (len(passport[5][1]) == 3 and passport[5][1] in eyeColor):
        return False
    if not (passport[6][1].isdigit() and len(passport[6][1]) == 9):
        return False
    return True

part1Score = 0
part2Score = 0
for passport in passports:
    if isValidPart1(passport):
        part1Score += 1
    if isValidPart2(passport):
        part2Score += 1
print(f"Part 1: {part1Score}")
print(f"Part 2: {part2Score}")