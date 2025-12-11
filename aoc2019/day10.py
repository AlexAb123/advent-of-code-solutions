from math import atan2, pi, dist

def solve(data):

    lines = data.split("\n")

    asteroids = set()
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == "#":
                asteroids.add((c, -r))
    
    part1 = 0
    for curr in asteroids:
        angles = set()
        detections = []
        for other in asteroids:
            if curr == other:
               continue 
            
            angle = (-1 * (atan2(curr[1] - other[1], curr[0] - other[0]) + pi / 2) * 180 / pi) % 360
            angles.add(angle)
            
            detections.append((angle, dist(curr, other), other))
            
        if len(angles) > part1:
            part1 = len(angles)
            best_detections = detections
            
    best_detections.sort()
    vaporized = []
    while len(vaporized) < len(asteroids) - 1:
        seen_angles = set()
        for angle, _, other in best_detections:
            if angle in seen_angles or other in vaporized:
                continue
            seen_angles.add(angle)
            vaporized.append(other)

    part2 = vaporized[199][0] * 100 - vaporized[199][1]
    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    data = (Path(__file__).parent/"inputs"/"day10.txt").read_text().strip()
    start = time()
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")