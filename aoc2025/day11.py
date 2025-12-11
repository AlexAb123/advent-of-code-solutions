from functools import cache

def solve(data):

    lines = [line.split(": ") for line in data.split("\n")]
    adjs = {device: set(adj.split(" ")) for device, adj in lines}
        
    @cache
    def dfs(curr, target):
        if curr == target:
            return 1
        return sum(dfs(adj, target) for adj in adjs.get(curr, set()))
    
    part1 = dfs("you", "out")
    part2 = dfs("svr", "dac") * dfs("dac", "fft") * dfs("fft", "out") + dfs("svr", "fft") * dfs("fft", "dac") * dfs("dac", "out")
    
    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    data = (Path(__file__).parent/"inputs"/"day11.txt").read_text().strip()
    start = time()
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")