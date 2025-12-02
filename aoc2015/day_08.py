from pathlib import Path

def solve():

    import re
    lines = Path(__file__).with_name('day_08_input.txt').open('r').read().strip().split("\n")

    part1 = 0
    part2 = 0
    for line in lines:

        line = line[1:len(line)-1]

        hexadecimal = re.findall(r"\\x[0-9-a-f]{2}", line)
        outside_quote = ['"', '"']
        quote = re.findall(r'\\\"', line)
        backslash = re.findall(r'\\\\', line)

        line_escape_length = sum(len(x) for x in hexadecimal + outside_quote + quote + backslash)
        line_string_length = len(line) - line_escape_length + len(hexadecimal) + len(quote) + len(backslash)
        
        part1 += len(line) - line_string_length
        
        part2 += len(hexadecimal) + 2*len(outside_quote) + 2*len(quote) + 2*len(backslash)

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")