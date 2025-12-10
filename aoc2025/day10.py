from heapq import heappush, heappop
from functools import cache
import numpy as np
from scipy.optimize import minimize, milp, linprog

def solve(data):

    def transform_button(button, length):
        new_button = [0 for _ in range(length)]
        for i in button:
            new_button[i] = 1
        return new_button
        
    lines = list(map(lambda x: x.split(" "), data.split("\n")))

    part1 = part2 = 0
    
    machines = []

    for line in lines:
        target = line[0][1:-1]
        buttons = []
        for button in line[1:-1]:
            button = list(map(int, button[1:-1].split(",")))
            button = transform_button(button, len(target))
            buttons.append(np.array(button, dtype=int))
        joltage = tuple(map(int, line[-1][1:-1].split(",")))
        machines.append((target, buttons, joltage))
    def adjs1(curr, buttons):
        curr = list(curr)
        for button in buttons:
            adj = curr.copy()
            for i in button:
                adj[i] = "#" if adj[i] == "." else "."
            yield "".join(adj)
            
    def bfs1(start, target, buttons):
        q = [(0, start)]
        seen = set([start])
        dist = 0
        while q:
            dist, curr = q.pop(0)
            if curr == target:
                return dist
            for adj in adjs1(curr, buttons):
                if adj in seen:
                    continue
                seen.add(adj)
                q.append((dist + 1, adj))
        return 0 # Shouldn't reach this
    
    def adjs2(curr, buttons, target):
        for button in sorted(buttons, key=lambda b: len(b)):
            adj = list(curr).copy()
            for i in button:
                adj[i] += 1
            yield tuple(adj), 1
    
    def adjs_part2(target, buttons):
        for button in buttons:
            t = list(target).copy()
            for i in button:
                t[i] -= 1
                yield tuple(t)
    @cache
    def dfs(target, buttons):
        if any(t < 0 for t in target):
            return float('inf')
        if all(t == 0 for t in target):
            return 0
        presses = float('inf')
        for new_target in adjs_part2(target, buttons):
            presses = min(presses, 1 + dfs(new_target, buttons))
        return presses
        
    def h(curr, target):
        return max(target[i] - curr[i] for i in range(len(curr)))
        
    def a_star(start, target, buttons):
      
        dists = {start: 0}
        visited = set()
        counter = 0
        q = [(h(start, target), counter, start)]
        while q:
            _, _, curr = heappop(q)
            
            if any(curr[i] > target[i] for i in range(len(curr))):
                continue
    
            if curr in visited: 
                continue
                
            visited.add(curr)
            
            if curr == target:
                return dists[curr]
                
            for adj, adj_dist in adjs2(curr, buttons, target):
                dist = dists[curr] + adj_dist
                if dist < dists.get(adj, float("inf")):
                    dists[adj] = dist
                    counter += 1
                    heappush(q, (dists[adj] + h(adj, target), counter, adj))
        return float("inf")
        
    def f(xs: np.ndarray):
        return int(np.sum(xs))
    def grad_f(xs: np.ndarray):
        return np.array(1 for _ in range(len(xs)))
        
    def g(xs: np.ndarray, buttons: list[np.ndarray], target: np.ndarray):
        total = target.copy()
        for i in range(len(xs)):
            x = xs[i]
            button = buttons[i]
            total = total - x * button
        return total
        
        

    #print(a_star((182, 180, 23, 44, 170, 66), (198, 181, 22, 50, 173, 65), {frozenset({0, 2, 4, 5}), frozenset({1, 3, 5}), frozenset({0, 1, 4}), frozenset({2, 3}), frozenset({4, 5}), frozenset({0, 2, 3, 5}), frozenset({0, 5}), frozenset({0, 3, 5})}))
    for machine in machines:
        #print(machine)
        part1 += bfs1("." * len(machine[0]), machine[0], machine[1])
        #part2 += dfs(machine[2], tuple(machine[1]))
        #part2 += a_star(tuple([0 for _ in range(len(machine[2]))]), machine[2], machine[1])
        
        
        
        buttons = machine[1]
        
        c = np.array([1 for _ in range(len(buttons))]) # Minimize c @ xs. This (array of 1s) would minimize the sum of xs
        integrality = np.array([1 for _ in range(len(buttons))]) # All xs must be integers
        # Transpose so that each button is its own column because ecah button is associated with 
        # one x (the number of times to press that specific button)
        A_eq = np.array([button for button in buttons]).T 
        for b in A_eq:
            print(b)
        b_eq = np.array(machine[2], dtype=int)
        bounds = [(0, None) for _ in range(len(c))]
        #A_eq = ({'type': 'eq', 'fun': lambda xs: g(xs, buttons, target)})
        res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, integrality=integrality)
        part2 += res.fun
    part2 = int(part2)
    return part1, part2
# 11860 too low, 20082 too low
if __name__ == "__main__":
    from pathlib import Path
    from time import time
    data = (Path(__file__).parent/"inputs"/"day10.txt").read_text().strip()
    start = time()
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")