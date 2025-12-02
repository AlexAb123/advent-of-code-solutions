from pathlib import Path

def solve():
        
    from collections import defaultdict
    lines = [line.split("-") for line in Path(__file__).with_name('day_23_input.txt').open('r').read().strip().split("\n")]

    adjs = defaultdict(set)
    for line in lines:
        adjs[line[0]].add(line[1])
        adjs[line[1]].add(line[0])

    all_nodes = set(adjs.keys())

    def get_interconnected_sets(group):
        if len(group) == 3:
            return {frozenset(group)}
        interconnected_sets = set()
        for adj in adjs[group[0]]:
            if adj in group or adj not in adjs[group[-1]]: # If it's not adjacent to the last node, then don't add it to group
                continue
            interconnected_sets.update(get_interconnected_sets(group + (adj,)))
        return interconnected_sets

    interconnected_sets = set()
    for node in all_nodes:
        if node[0] != "t":
            continue
        interconnected_sets.update(get_interconnected_sets((node,)))
    part1 = len(interconnected_sets)
        
    cliques = set()
    for node in all_nodes:
        if cliques and len(adjs[node]) <= len(max(cliques, key=len)):
            continue
        clique = {node}
        for adj in adjs[node]:
            add_to_clique = True
            for clique_node in clique:
                if adj not in adjs[clique_node]:
                    add_to_clique = False
                    break
            if add_to_clique:
                clique.add(adj)
        cliques.add(frozenset(clique))

    part2 = ",".join(sorted(list(max(cliques, key=len))))

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")