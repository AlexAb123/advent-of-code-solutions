from pathlib import Path

def solve():

    import re

    lines = Path(__file__).with_name('day_21_input.txt').open('r').read().strip().split("\n")

    def scramble(password, instructions):

        password = list(password)
        for instruction in instructions:
        
            if "swap position" in instruction:
                x, y = map(int, re.findall(r"position (\d+)", instruction))
                password[x], password[y] = password[y], password[x]

            elif "swap letter" in instruction:
                x, y = map(lambda c: password.index(c), re.findall(r"letter (\w+)", instruction))
                password[x], password[y] = password[y], password[x]
                
            elif "rotate right" in instruction:
                steps = int(re.findall(r"rotate right (\d+)", instruction)[0]) % len(password)
                password = password[-steps:] + password[:-steps]

            elif "rotate left" in instruction:
                steps = int(re.findall(r"rotate left (\d+)", instruction)[0]) % len(password)
                password = password[steps:] + password[:steps]

            elif "rotate based" in instruction:
                x = re.findall(r"letter (\w+)", instruction)[0]
                steps = password.index(x)
                if steps >= 4:
                    steps += 1
                steps += 1
                steps = steps % len(password)
                password = password[-steps:] + password[:-steps]

            elif "reverse positions" in instruction:
                x = int(re.findall(r"positions (\d+)", instruction)[0])
                y = int(re.findall(r"through (\d+)", instruction)[0]) + 1
                password = password[:x] + password[x:y][::-1] + password[y:]
                
            elif "move position" in instruction:
                x, y = map(int, re.findall(r"position (\w+)", instruction))
                password.insert(y, password.pop(x))

        return "".join(password)
    
    part1 = scramble("abcdefgh", lines)

    from itertools import permutations
    for p in permutations("abcdefgh"): # Brute force search for a password that equals "fbgdceah" after scrambling
        if scramble("".join(p), lines) == "fbgdceah":
            part2 = "".join(p)
            break

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")