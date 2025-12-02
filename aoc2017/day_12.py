from pathlib import Path

def solve():

    from collections import defaultdict
    lines = [line.split(" <-> ") for line in Path(__file__).with_name('day_12_input.txt').open('r').read().strip().split("\n")]

    adjs = defaultdict(set)
    for line in lines:
        for adj in line[1].split(", "):
            adjs[int(line[0])].add(int(adj))
            adjs[int(adj)].add(int(line[0]))

    def bfs(source):
        q = [source]
        visited = {source}
        while q:
            curr = q.pop(0)
            for adj in adjs[curr]:
                if adj in visited:
                    continue
                visited.add(adj)
                q.append(adj)
        return frozenset(visited)

    part1 = len(bfs(0))
    groups = set()
    for num in adjs:
        groups.add(bfs(num))
    part2 = len(groups)

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")