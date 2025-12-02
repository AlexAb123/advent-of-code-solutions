from pathlib import Path
lines = Path(__file__).with_name('day_04_input.txt').open('r').read().strip()

import hashlib

def md5(value):
    return hashlib.md5(value.encode()).hexdigest()

def hasXLeadingZeros(string, x):
    for i in range(x):
        if string[i] != "0":
            return False
    return True

num = 0
while not hasXLeadingZeros(md5(lines + str(num)), 5):
    num += 1
print(f"Part 1: {num}")
num = 0
while not hasXLeadingZeros(md5(lines + str(num)), 6):
    num += 1
print(f"Part 2: {num}")