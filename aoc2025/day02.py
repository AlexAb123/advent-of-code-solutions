def solve(input_path):
    
    line = input_path.open('r').read().strip().split(",")

    part1 = 0
    part2 = 0

    def valid1(id):
        return id[:len(id) // 2] != id[len(id) // 2:]
    
    def valid2(id):
        for length in range(1, len(id) // 2 + 1):
            if (id == id[:length] * (len(id) // length)):
                return False
        return True
    
    for r in line:
        start, end = map(int, r.split("-"))
        for id in range(start, end + 1):
            if not valid1(str(id)):
                part1 += id
            if not valid2(str(id)):
                part2 += id
                
    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    start = time()
    part1, part2 = solve(Path(__file__).parent/"inputs"/"day02.txt")
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")