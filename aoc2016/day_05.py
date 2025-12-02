from pathlib import Path

def solve():

    from hashlib import md5

    door = Path(__file__).with_name('day_05_input.txt').open('r').read().strip()

    i = 0
    part1 = ""
    part2 = ["", "", "", "", "", "", "", ""]
    while any(elt == "" for elt in part2) or len(part1) < 8:
        while md5((door + str(i)).encode("utf-8")).hexdigest()[:5] != "00000":
            i += 1
        code = md5((door + str(i)).encode("utf-8")).hexdigest()
        part1 += code[5]
        if (code[5].isdigit() and int(code[5]) < 8 and part2[int(code[5])] == ""):
            part2[int(code[5])] = code[6]
        i += 1
    part2 = "".join(part2)

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")