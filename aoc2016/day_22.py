from pathlib import Path

def solve():

    import re
    from collections import defaultdict

    lines = Path(__file__).with_name('day_22_input.txt').open('r').read().strip().split("\n")[2:]

    nodes = {}

    for line in lines:
        x, y = map(int, re.findall(r"x(\d+)-y(\d+)", line)[0])
        pos = x + y * 1j
        data = list(map(int, re.findall(r" (\d+)", line)))
        data = {"size": data[0], "used": data[1], "avail": data[2], "use%": data[3]}
        nodes[pos] = data

    part1 = 0
    adjs = defaultdict(set)
    for node1 in nodes:
        for node2 in nodes:
            if node1 == node2:
                continue
            if nodes[node1]["used"] != 0 and nodes[node1]["used"] <= nodes[node2]["avail"]:
                adjs[node1].add(node2)
                part1 += 1
    print(adjs)

    q = [(max(nodes.keys(), key=lambda node: node.real), 0)]
    seen = set()
    print(q)
    part2 = 0
    while q:
        print(q)
        curr, dist = q.pop(0)
        seen.add(curr)

        if curr == 0 + 0j:
            part2 = dist
            print("FOUND")
            break
        print(curr)
        for adj in adjs[curr]:
            if adj in seen:
                continue
            q.append((adj, dist + 1))


    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")