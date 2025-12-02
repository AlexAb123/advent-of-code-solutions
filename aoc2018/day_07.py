from pathlib import Path

def solve():
        
    from collections import defaultdict
    lines = [line.split(" ") for line in Path(__file__).with_name('day_07_input.txt').open('r').read().strip().split("\n")]
    adjs = defaultdict(list)
    nodes = set()
    in_degree_initial = defaultdict(int)
    for line in lines:
        adjs[line[1]].append(line[-3])
        nodes.add(line[1])
        nodes.add(line[-3])
        in_degree_initial[line[-3]] += 1

    in_degree = in_degree_initial.copy()
    for curr in adjs:
        adjs[curr] = sorted(adjs[curr])

    from heapq import heappop, heappush
    pq = []
    for node in nodes:
        if in_degree[node] == 0:
            heappush(pq, node)

    # Lexicographical Topological Sort using Kahn's Algorithm
    order = []
    while pq:
        curr = heappop(pq)
        order.append(curr)
        for adj in adjs[curr]:
            in_degree[adj] -= 1
            if in_degree[adj] == 0:
                heappush(pq, adj)

    part1 = "".join(order)

    def time_to_complete(node):
        return 60 + ord(node) - 64
    
    in_degree = in_degree_initial.copy()
    part2 = 0
    completed = set()
    in_progress = []
    construction_time = defaultdict(int)
    while len(completed) < len(nodes):
        print(in_progress)
        for curr in nodes.copy():
            if curr in completed or curr in in_progress:
                continue
            if in_degree[curr] == 0:
                in_progress.append(curr)

        for curr in in_progress[:5]:
            construction_time[curr] += 1
            if construction_time[curr] == time_to_complete(curr):
                completed.add(curr)
                in_progress.remove(curr)
                for adj in adjs[curr]:
                    in_degree[adj] -= 1
        part2 += 1

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")