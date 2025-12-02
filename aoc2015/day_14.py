from pathlib import Path

def solve():

    from collections import defaultdict

    lines = Path(__file__).with_name('day_14_input.txt').open('r').read().strip().split("\n")

    reindeer = set()
    for line in lines:
        name = line.split(" ")[0]
        speed = int(line.split(" ")[3])
        move_time = int(line.split(" ")[6])
        rest_time = int(line.split(" ")[-2])
        reindeer.add((name, speed, move_time, rest_time))

    max_time = 2503

    reindeer_scores = defaultdict(int)
    for second in range(1, max_time+1):

        dists = defaultdict(set)

        for deer in reindeer:
            cycles = second//(deer[2]+deer[3])
            remainder = second%(deer[2]+deer[3])
            dist = cycles * deer[1] * deer[2]
            if remainder > 0:
                dist += deer[1] * min(remainder, deer[2])
            dists[dist].add(deer[0])
        
        for deer in dists[max(dists.keys())]:
            reindeer_scores[deer] += 1

        if second == max_time:
            part1 = max(dists.keys())

    part2 = max(reindeer_scores.values())

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")