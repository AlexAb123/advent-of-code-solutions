from pathlib import Path

def solve():
    lines = [list(map(int, line.replace(":", "").split(" "))) for line in Path(__file__).with_name('day_07_input.txt').open('r').read().strip().split("\n")]

    def check(target, nums, part2):
        if target < nums[-1]:
            return False
        if len(nums) == 1:
            return nums[-1] == target
        if check(target-nums[-1], nums[:-1], part2):
            return True
        if target % nums[-1] == 0 and check(target//nums[-1], nums[:-1], part2):
            return True
        if part2 and target != nums[-1] and str(target).endswith(str(nums[-1])) and check(int(str(target).removesuffix(str(nums[-1]))), nums[:-1], part2):
            return True
        return False
    
    part1 = 0
    part2 = 0
    for line in lines:
        if check(line[0], line[1:], False):
            part1 += line[0]
            part2 += line[0]
        elif check(line[0], line[1:], True):
            part2 += line[0]
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")