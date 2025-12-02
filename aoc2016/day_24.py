from pathlib import Path

def solve():

    lines = Path(__file__).with_name('day_24_input.txt').open('r').read().strip().split("\n")

    passages = set() 
    targets = []
    start = 0
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c].isdigit():
                targets.append(r+c*1j)
                passages.add(r+c*1j)
                if lines[r][c] == "0":
                    start = r+c*1j
            elif lines[r][c] == ".":
                passages.add(r+c*1j)
            
    def get_adjs(curr):
        for d in 1,-1,1j,-1j:
            yield curr + d

    def bfs(source, target):
        visited = {source}
        q = [(0, source)]
        while q:
            dist, curr = q.pop(0)
            if curr == target:
                break
            for adj in get_adjs(curr):
                if adj in visited or adj not in passages:
                    continue
                visited.add(adj)
                q.append((dist + 1, adj))
        return dist

    from collections import defaultdict
    adjacency_matrix = defaultdict(set)
    for i in range(len(targets)):
        for j in range(i+1, len(targets)):
            dist = bfs(targets[i], targets[j])
            adjacency_matrix[targets[i]].add((dist, targets[j]))
            adjacency_matrix[targets[j]].add((dist, targets[i]))

    def dfs1(curr, visited, dist):
        visited.add(curr)
        if len(visited) == len(targets):
            return {dist}
        dists = set()
        for adj_dist, adj in adjacency_matrix[curr]:
            if adj in visited:
                continue
            dists.update(dfs1(adj, visited.copy(), dist+adj_dist))
        return dists

    def dfs2(curr, visited, dist, add_to_visited, start):
        if add_to_visited:
            visited.add(curr)
        if len(visited) == len(targets):
            if curr == start:
                return {dist}
            else:
                return {}
        dists = set()
        for adj_dist, adj in adjacency_matrix[curr]:
            if adj in visited:
                continue
            dists.update(dfs2(adj, visited.copy(), dist+adj_dist, True, start))
        return dists

    part1 = min(dfs1(start, set(), 0))
    part2 = min(dfs2(start, set(), 0, False, start))

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")