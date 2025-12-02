from pathlib import Path

def solve():

    from hashlib import md5
    import re

    salt = Path(__file__).with_name('day_14_input.txt').open('r').read().strip()

    print(salt)

    part1 = 0
    part2 = 0

    i = 18
    keys = []
    hashes = []
    while len(keys) < 1:
        if hashes:
            previous = hashes.pop(0)

        curr = md5((salt + str(i)).encode("utf-8")).hexdigest()
        
        
        
        hashes.append((frozenset(re.findall(r"(\w)\1{2}", curr)), frozenset(re.findall(r"(\w)\1{4}", curr))))
        print(hashes)
        keys.append(0)
        i += 1

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")