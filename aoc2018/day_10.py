from pathlib import Path

def solve():

    import re

    lines = Path(__file__).with_name('day_10_input.txt').open('r').read().strip().split("\n")

    points = set()
    for line in lines:
        pos, vel = re.findall(r"<(.*?)>", line)
        pos = tuple(map(int, pos.split(",")[::-1]))
        vel = tuple(map(int, vel.split(",")[::-1]))
        points.add((pos, vel))

    def update(points):
        new_points = set()
        for point in points:
            new_points.add(((point[0][0] + point[1][0], point[0][1] + point[1][1]), (point[1][0], point[1][1])))
        return new_points
    
    def normalize(points):
        min_row = min(point[0][0] for point in points)
        min_col = min(point[0][1] for point in points)
        new_points = set()
        for point in points:
            new_points.add(((point[0][0] - min_row, point[0][1] - min_col), point[1]))
        return new_points

    def visualize(points):
        grid = [["." for _ in range(max(point[0][1] for point in points) + 1)] for _ in range(max(point[0][0] for point in points) + 1)]
        for point in points:
            grid[point[0][0]][point[0][1]] = "#"
        string = ""
        for line in grid:
            string += "".join(line) + "\n"
        return string
    
    def adjacent_count(points):
        total = 0
        positions = set(point[0] for point in points)
        for pos in positions:
            for dr, dc in (1, 0), (-1, 0), (0, 1), (0, -1):
                if (pos[0] + dr, pos[1] + dc) in positions:
                    total += 1
        return total

    points = normalize(points)
    rows = max(point[0][0] for point in points)
    cols = max(point[0][1] for point in points)
    part1 = None
    part2 = 0
    while True:
        new_points = normalize(update(points))
        if rows < max(point[0][0] for point in new_points) and cols < max(point[0][1] for point in new_points):
            part1 = "\n" + visualize(points)
            break
        points = new_points
        rows = max(point[0][0] for point in points)
        cols = max(point[0][1] for point in points)
        part2 += 1

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")