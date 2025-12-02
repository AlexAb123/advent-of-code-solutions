from pathlib import Path
lines = Path(__file__).with_name('day 1 input.txt').open('r').read().strip().split("\n")

def part1():
    total = 0
    for string in lines:
        current = ""
        for f in range(len(string)):
            if string[f].isdigit():
                current += string[f]
                break
        for l in reversed(range(len(string))):
            if string[l].isdigit():
                current += string[l]
                break
        total += int(current)

    print(f"Part 1: {total}")

def part2():
    digits = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":'8',"nine":'9'}
    total = 0
    for string in lines:
        current = ""
        for f in range(len(string)):
            if string[f].isdigit():
                current += string[f]
                break
            if string[f:f+3] in digits:
                current += digits[string[f:f+3]]
                break
            if string[f:f+4] in digits:
                current += digits[string[f:f+4]]
                break
            if string[f:f+5] in digits:
                current += digits[string[f:f+5]]
                break
            if string[f:f+6] in digits:
                current += digits[string[f:f+6]]
                break
        for l in reversed(range(len(string))):
            if string[l].isdigit():
                current += string[l]
                break
            if string[l].isdigit():
                current += string[l]
                break
            if string[l:l+3] in digits:
                current += digits[string[l:l+3]]
                break
            if string[l:l+4] in digits:
                current += digits[string[l:l+4]]
                break
            if string[l:l+5] in digits:
                current += digits[string[l:l+5]]
                break
            if string[l:l+6] in digits:
                current += digits[string[l:l+6]]
                break
        total += int(current)
    print(f"Part 2: {total}")

part1()
part2()