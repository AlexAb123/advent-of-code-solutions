from pathlib import Path

def solve():

    from collections import defaultdict
    lines = Path(__file__).with_name('day_09_input.txt').open('r').read().strip().split("\n")

    adjs = defaultdict(set)

    for line in lines:
        nodes, dist = line.split(" = ")
        source, target = nodes.split(" to ")
        adjs[source].add((int(dist), target))
        adjs[target].add((int(dist), source))

    nodes = set(adjs.keys())

    def get_dists(curr, dist, visited):
        visited.add(curr)
        if len(visited) == len(nodes):
            return {dist}
        dists = set()
        for adj_dist, adj in adjs[curr]:
            if adj in visited:
                continue
            dists.update(get_dists(adj, dist+adj_dist, visited.copy()))

        return dists

    dists = set()
    for node in nodes:
        dists.update(get_dists(node, 0, set()))
    part1 = min(dists)
    part2 = max(dists)

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")