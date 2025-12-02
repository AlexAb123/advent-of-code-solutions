from pathlib import Path

def solve():

    from collections import defaultdict, Counter

    lines = Path(__file__).with_name('day_07_input.txt').open('r').read().strip().split("\n")

    all_nodes = set()
    end_nodes = set()
    adjs = defaultdict(set)
    parents = {}
    initial_weights = {}
    weights = {}
    for line in lines:
        name, line = line.split(" (")
        all_nodes.add(name)
        weight, line = line.split(")")
        weights[name] = int(weight)
        initial_weights[name] = int(weight)
        if line:
            for adj in line[4:].split(", "):
                adjs[name].add(adj)
                parents[adj] = name
        else:
            end_nodes.add(name)
    seen = set()
    for curr in adjs:
        seen.update(adjs[curr])
    
    part1 = list(all_nodes - seen)[0]

    def calculate_weight(curr):
        weights[curr] = weights[curr] + sum(calculate_weight(adj) for adj in adjs[curr])
        return weights[curr]
    calculate_weight(part1)

    q = list(end_nodes)
    done = False
    while q and not done:
        curr = q.pop(0)
        if curr in parents and parents[curr] not in q:
            q.append(parents[curr])
        branches = defaultdict(set)
        for adj in adjs[curr]:
            branches[weights[adj]].add(adj)
        for weight, branch in branches.items():
            if len(branch) == 1:
                wrong_program = list(branch)[0]
                part2 = initial_weights[wrong_program] - max(branches.keys()) + min(branches.keys())
                done = True
                break
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")