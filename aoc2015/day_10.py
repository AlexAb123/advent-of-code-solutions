from pathlib import Path

def solve():

    num = Path(__file__).with_name('day_10_input.txt').open('r').read().strip()

    def get_new_num(num):
        new_num = ""
        acc, acc_char = 0, num[0]
        for char in num:
            if char == acc_char:
                acc += 1
            else:
                new_num += str(acc) + acc_char
                acc_char = char
                acc = 1
        new_num += str(acc) + acc_char
        return new_num
    
    for i in range(50):
        num = get_new_num(num)
        if i == 39:
            part1 = len(num)
    part2 = len(num)

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")