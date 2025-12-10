import numpy as np
from scipy.optimize import linprog

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
            buttons.append(button)
        joltage = tuple(map(int, line[-1][1:-1].split(",")))
        machines.append((target, buttons, joltage))
        
    def adjs(curr, buttons):
        curr = list(curr)
        for button in buttons:
            adj = curr.copy()
            for i in button:
                adj[i] = "#" if adj[i] == "." else "."
            yield "".join(adj)
            
    def bfs(start, target, buttons):
        q = [(0, start)]
        seen = set([start])
        dist = 0
        while q:
            dist, curr = q.pop(0)
            if curr == target:
                return dist
            for adj in adjs(curr, buttons):
                if adj in seen:
                    continue
                seen.add(adj)
                q.append((dist + 1, adj))
        return 0 # Shouldn't reach this
        
    for machine in machines:
        part1 += bfs("." * len(machine[0]), machine[0], machine[1])
        
        buttons = [transform_button(button, len(machine[2])) for button in machine[1]]
        c = np.array([1 for _ in range(len(buttons))]) # Minimize c @ xs. This (array of 1s) would minimize the sum of xs
        integrality = np.array([1 for _ in range(len(buttons))]) # All xs must be integers
        
        # Transpose so that each button is its own column because each button is associated with 
        # one x (the number of times to press that specific button)
        # For first example input:
        # [[0, 0, 0, 0, 1, 1],
        #  [0, 1, 0, 0, 0, 1],
        #  [0, 0, 1, 1, 1, 0],
        #  [1, 1, 0, 1, 0, 0]]
        # where each column is a button (first column is the button '(3)', second is the button '(1, 3)')
        # 
        # Multiplied by
        # [x1, x2, x3, x4, x5, x6]
        # 
        # Has to equal the target 
        # [3, 5, 4, 7]
        # 
        # So A_eq is the first matrix, and b_eq is the target
        A_eq = np.array([button for button in buttons]).T
        b_eq = np.array(machine[2], dtype=int)
        bounds = [(0, None) for _ in range(len(c))]
        res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, integrality=integrality)
        part2 += res.fun
        
    part2 = int(part2)
    return part1, part2
    
if __name__ == "__main__":
    from pathlib import Path
    from time import time
    data = (Path(__file__).parent/"inputs"/"day10.txt").read_text().strip()
    start = time()
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")