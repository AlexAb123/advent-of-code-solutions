from pathlib import Path

def solve():

    import json

    json_string = Path(__file__).with_name('day_12_input.txt').open('r').read().strip()

    obj = json.loads(json_string)

    def find_sum(obj, part2):
        if type(obj) == int:
            return obj

        if type(obj) == list:
            total = 0
            for o in obj:
                total += find_sum(o, part2)
            return total
        
        if type(obj) == dict:
            total = 0
            for v in obj.values():
                if part2 and v == "red":
                    return 0
                total += find_sum(v, part2)
            return total
        
        return 0

    part1 = find_sum(obj, False)
    part2 = find_sum(obj, True)
    
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")
