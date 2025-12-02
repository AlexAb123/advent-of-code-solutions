from pathlib import Path
lines = Path(__file__).with_name('day_05_input.txt').open('r').read().strip().split("\n")

def countVowels(string):
    vowels = 0
    for character in string:
        if character in "aeiou":
            vowels += 1
    return vowels

def hasDoubleLetter(string):
    for i in range(1, len(string)):
        if string[i-1] == string[i]:
            return True
    return False

def doesNotHave(string):
    for i in range(1, len(string)):
        if string[i-1:i+1] in ["ab", "cd", "pq", "xy"]:
            return False
    return True

def hasPairNoOverlap(string):
    for i in range(len(string)-1):
        for j in range(i+2, len(string)-1):
            if string[i:i+2] == string[j:j+2]:
                return True
    return False

def hasDoubleLetterOneInBetween(string):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False


part1 = 0
for string in lines:
    if countVowels(string) >= 3 and hasDoubleLetter(string) and doesNotHave(string):
        part1 += 1
print(f"Part 1: {part1}")

part2 = 0
for string in lines:
    if hasPairNoOverlap(string) and hasDoubleLetterOneInBetween(string):
        part2 += 1
print(f"Part 2: {part2}")