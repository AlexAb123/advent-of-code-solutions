from pathlib import Path

def solve():

    lines = Path(__file__).with_name('day_10_input.txt').open('r').read().strip().split("\n")

    def count_trailhead_score(pos, seen):

        value = int(lines[pos[0]][pos[1]])
        if value == 9:
            if pos in seen:
                return 0, 1
            seen.add(pos)
            return 1, 1
        
        adjacents = set({(pos[0] + dr, pos[1] + dc) for dr, dc in ((1,0), (-1,0), (0,1), (0,-1))})
        part1_score, part2_score = 0, 0
        for adj in adjacents:
            if not (0 <= adj[0] < len(lines) and 0 <= adj[1] < len(lines[0])):
                continue
            if int(lines[adj[0]][adj[1]]) - value == 1:
                new_part1_score, new_part2_score = count_trailhead_score(adj, seen)
                part1_score += new_part1_score
                part2_score += new_part2_score
        return part1_score, part2_score
    
    part1, part2 = 0, 0
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if int(lines[r][c]) == 0:
                new_part1, new_part2 = count_trailhead_score((r,c), set())
                part1 += new_part1
                part2 += new_part2
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")