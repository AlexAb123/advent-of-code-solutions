from pathlib import Path

def solve():
    from collections import defaultdict

    lines = [line.split("-") for line in Path(__file__).with_name('day_12_input.txt').open('r').read().strip().split("\n")]
    
    small_caves = set()
    big_caves = set()
    adjacents = defaultdict(set)
    for line in lines:
        adjacents[line[0]].add(line[1])
        adjacents[line[1]].add(line[0])

        for cave in line:
            if cave == cave.lower():
                small_caves.add(cave)
            else:
                big_caves.add(cave)
    start = "start"
    end = "end"

    def find_path_count(current, visited, part2, small_cave_twice=False):
        if current == end:
            return 1

        visited[current] += 1
        path_count = 0

        for adj in adjacents[current]:

            if part2:

                if adj == start:
                    continue
                if adj in small_caves and visited[adj] == 1 and not small_cave_twice:
                    path_count += find_path_count(adj, visited.copy(), part2, True)
                elif adj in small_caves and visited[adj] == 0:
                    path_count += find_path_count(adj, visited.copy(), part2, small_cave_twice)
                elif adj in big_caves:
                    path_count += find_path_count(adj, visited.copy(), part2, small_cave_twice)

            else:
                if adj in small_caves and adj in visited:
                    continue
                path_count += find_path_count(adj, visited.copy(), part2)
        
        return path_count

    part1 = find_path_count(start, defaultdict(int), False)
    part2 = find_path_count(start, defaultdict(int), True)
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")