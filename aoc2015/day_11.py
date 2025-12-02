from pathlib import Path

def solve():
        
    password = list(Path(__file__).with_name('day_11_input.txt').open('r').read().strip())

    def is_valid(password):

        if "i" in password or "o" in password or "l" in password:
            return False
        
        i = 0
        pairs = 0
        while i < len(password)-1:
            if password[i] == password[i+1]:
                pairs += 1
                i += 2
            else:
                i += 1
        if pairs < 2:
            return False

        straight = False
        for i in range(len(password)-2):
            ords = tuple(map(ord, password[i:i+3]))
            if tuple(map(lambda x: x-min(ords), ords)) == (0, 1, 2):
                straight = True
                break
        if not straight:
            return False

        return True

    def increment_password(password):
        new_password = password.copy()
        for i in range(len(password)-1, -1, -1):
            if password[i] != "z":
                new_password[i] = chr(ord(password[i])+1)
                break
            else:
                new_password[i] = "a"
        return new_password

    while not is_valid(password):
        password = increment_password(password)
    part1 = "".join(password)
    password = increment_password(password)
    while not is_valid(password):
        password = increment_password(password)
    part2 = "".join(password)

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")