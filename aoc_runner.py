    
def run(solve, file):
    from pathlib import Path
    from time import time
    filepath = Path(file)
    data = (filepath.parent/"inputs"/f"{filepath.stem}.txt").read_text().strip()
    start = time()
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")