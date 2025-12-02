from pathlib import Path

def solve():
    lines = [tuple(map(int, reversed(line.split(",")))) for line in Path(__file__).with_name('day_18_input.txt').open('r').read().strip().split("\n")]

    def in_bounds(pos):
        return start[0] <= pos[0] <= end[0] and 0 <= pos[1] <= end[1]
    
    def get_adjs(pos):
        for dr, dc in (1,0), (-1,0), (0,1), (0,-1):
            yield (pos[0]+dr,pos[1]+dc)

    def shortest_distance(start, end, corrupted):
        visited = set()
        q = [(start, 0)]
        while q:
            curr, dist = q.pop(0)
            if curr == end:
                return dist
            for adj in get_adjs(curr):
                if adj in corrupted or adj in visited or not in_bounds(adj):
                    continue
                visited.add(adj)
                q.append((adj, dist+1))
        return float('inf')

    start = (0,0)
    end = (70,70)
    corrupted = set()
    for i in range(1024):
        corrupted.add(lines[i])

    def get_corrupted_n_steps(steps):
        new_corrupted = corrupted.copy()
        for i in range(1024, steps):
            new_corrupted.add(lines[i])
        return new_corrupted

    def binary_search(low, high):
        mid = (high-low)//2 + low
        curr_result = shortest_distance(start, end, get_corrupted_n_steps(mid))
        prev_result = shortest_distance(start, end, get_corrupted_n_steps(mid-1))
        if curr_result == float('inf') and prev_result != float('inf'):
            return mid
        if curr_result == float('inf'):
            return binary_search(low, mid-1)
        elif prev_result != float('inf'):
            return binary_search(mid+1, high)

    part1 = shortest_distance(start, end, corrupted)
    part2 = ",".join(map(str, (lines[binary_search(1024, len(lines))-1][::-1])))
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")