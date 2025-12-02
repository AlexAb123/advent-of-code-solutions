from pathlib import Path

def solve():

    from operator import add, mul
    from collections import deque
    lines = [deque(line.replace(" ", "")) for line in Path(__file__).with_name('day_18_input.txt').open('r').read().strip().split("\n")]
    def evaluate1(line, acc=0, op=add):

        if len(line) == 0:
            return acc
        
        first = line.popleft()

        if first.isdigit():
            return evaluate1(line, op(acc, int(first)))
        
        if first in "+*":
            op = add if first == "+" else mul
            return evaluate1(line, acc, op)
        
        if first == "(":
            new_acc, rest_line = evaluate1(line)
            return evaluate1(rest_line, op(acc, new_acc))
                    
        if first == ")":
            return acc, line

    part1 = sum(evaluate1(line) for line in lines)

    def evaluate2(line, acc=0, op=add):

        if len(line) == 0:
            return acc
        
        first = line.popleft()

        if first.isdigit():
            return evaluate2(line, op(acc, int(first)))
        
        if first in "+*":
            op = add if first == "+" else mul
            return evaluate2(line, acc, op)
        
        if first == "(":
            new_acc, rest_line = evaluate2(line)
            return evaluate2(rest_line, op(acc, new_acc))
                    
        if first == ")":
            return acc, line
        
    part2 = sum(evaluate2(line) for line in lines)

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")