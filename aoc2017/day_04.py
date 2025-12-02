from pathlib import Path

def solve():
    from collections import Counter
    passphrases = [passphrase.split(" ") for passphrase in Path(__file__).with_name('day_04_input.txt').open('r').read().strip().split("\n")]

    def valid_passphrase(passphrase, part2):

        if not part2:
            return len(set(passphrase)) == len(passphrase)
        
        else:
            for i in range(len(passphrase)):
                for j in range(i+1, len(passphrase)):
                    if Counter(passphrase[i]) == Counter(passphrase[j]):
                        return False
            return True

    part1 = sum(valid_passphrase(passphrase, False) for passphrase in passphrases)
    part2 = sum(valid_passphrase(passphrase, True) for passphrase in passphrases)
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")