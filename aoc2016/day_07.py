from pathlib import Path

def solve():

    import re

    lines = Path(__file__).with_name('day_07_input.txt').open('r').read().strip().split("\n")

    def has_abba(string):
        if len(string) < 4:
            return False
        for i in range(len(string)-3):
            if string[i] == string[i+3] and string[i+1] == string[i+2] and string[i] != string[i+1]:
                return True
        return False
    
    def find_aba(string):
        aba = set()
        if len(string) < 3:
            return aba
        for i in range(len(string)-2):
            if string[i] == string[i+2] and string[i] != string[i+1]:
                aba.add(string[i:i+3])
        return aba
    
    part1 = 0
    part2 = 0
    for line in lines:
        outside = re.sub(r"\[(.*?)\]", " ", line).split(" ")
        inside = re.findall(r"\[(.*?)\]", line)
      
        if all(not has_abba(string) for string in inside) and any(has_abba(string) for string in outside):
            part1 += 1

        found = False
        abas = set()
        for string in outside:
            for aba in find_aba(string):
                abas.add(aba)
        for aba in abas:
            for string in inside:
                if len(re.findall(aba[1] + aba[0] + aba[1], string)) > 0:
                    part2 += 1
                    found = True
                    break
            if found:
                break
      
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")