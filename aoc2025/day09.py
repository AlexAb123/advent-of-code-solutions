from itertools import combinations
from heapq import heapify_max, heappop_max

def solve(data):

    lines = list(map(lambda line: tuple(map(int, line.split(",")[::-1])), data.split("\n")))
    combos = list(combinations(lines, 2))
    num_points = len(lines)
    #part1 = max((abs(r1 - r2) + 1) * (abs(c1 - c2) + 1) for (r1, c1), (r2, c2) in combos)

    # Gives the index of a given point. Inverse of lines. Lines would be index to point
    point_to_index = {p: i for i, p in enumerate(lines)}

    rectangles = [] # Stores tuples of (area, p1_index, p2_index)
    for p1, p2 in combos:
        r1, c1 = p1
        r2, c2 = p2
        rectangles.append(((abs(r1 - r2) + 1) * (abs(c1 - c2) + 1), point_to_index[p1], point_to_index[p2]))
    heapify_max(rectangles)

    # Part 1 is the area of the largest rectangle
    part1 = rectangles[0][0]


    row_pad = 1 # Add padding so we can move around the outside of the polygon
    col_pad = 1


    # Compress the grid by only keeping the coordinates that have red tiles
    unique_rows = sorted(set(r for r, c in lines))
    unique_cols = sorted(set(c for r, c in lines))
    row_to_idx = {r: i for i, r in enumerate(unique_rows)}
    col_to_idx = {c: i for i, c in enumerate(unique_cols)}
    compressed_points = [(row_to_idx[r] + row_pad, col_to_idx[c] + col_pad) for r, c in lines]

    max_r = max(r for r, c in compressed_points)
    max_c = max(c for r, c in compressed_points)
    
    rows = max_r + 2 * row_pad
    cols = max_c + 2 * col_pad

    # Generate and store the sides of the polygon
    sides = set()
    corners = set(compressed_points)
    for i in range(len(compressed_points)):
        r1, c1 = compressed_points[i]
        r2, c2 = compressed_points[(i+1)%num_points]
        if r1 == r2:
            for c in range(min(c1, c2)+1, max(c1, c2)):
                sides.add((r1, c))
        else:
            for r in range(min(r1, r2)+1, max(r1, r2)):
                sides.add((r, c1))

    # Flood fill the outside of the polygon
    outside = set()
    q = [(0, 0)] # We know 0, 0 is not inside the polygon because we added padding
    while q:
        curr = q.pop(0)
        r, c = curr
        for dr, dc in (1, 0), (-1, 0), (0, 1), (0, -1):
            ar, ac = r + dr, c + dc
            adj = (ar, ac)
            if not (0 <= ar < rows and 0 <= ac < cols):
                continue
            if adj in outside or adj in corners or adj in sides:
                continue
            q.append(adj)
            outside.add(adj)

    """ grid = [["." for _ in range(cols)] for _ in range(rows)]
    for r, c in sides | corners:
        grid[r - min_r + row_pad][c - min_c + col_pad] = "#"
    for r, c in outside:
        grid[r][c] = "X"
    for l in grid:
        print("".join(l)) """
    
    # 2D array where the outside is 0 and the inside of the polygon is 1
    inside = [[1 for _ in range(cols)] for _ in range(rows)]
    for r, c in outside:
        inside[r][c] = 0

    prefix_sum = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            prefix_sum[r][c] = inside[r-1][c-1] + prefix_sum[r-1][c] + prefix_sum[r][c-1] - prefix_sum[r-1][c-1]
    def query_prefix_sum(r1, c1, r2, c2): # Assumes (r1, c1) is the top left.
        return prefix_sum[r2+1][c2+1] - prefix_sum[r2+1][c1] - prefix_sum[r1][c2+1] + prefix_sum[r1][c1]
    part2 = 0
    print(prefix_sum)
    def rectangle_area(p1, p2):
        r1, c1 = p1
        r2, c2 = p2
        return (abs(r1 - r2) + 1) * (abs(c1 - c2) + 1)
    
    # For every rectangle, check if any of the tiles in its perimeter is outside. If yes, then it is not a valid rectangle
    while True:
        area, p1_idx, p2_idx = heappop_max(rectangles)
        p1 = compressed_points[p1_idx]
        p2 = compressed_points[p2_idx]
        r1, c1 = p1
        r2, c2 = p2

        valid = True
        for c in range(min(c1, c2), max(c1, c2) + 1):
            if (r1, c) in outside:
                valid = False
                break
            if (r2, c) in outside:
                valid = False
                break
        if not valid:
            continue
        
        for r in range(min(r1, r2), max(r1, r2) + 1):
            if (r, c1) in outside:
                valid = False
                break
            if (r, c2) in outside:
                valid = False
                break
        if valid:
            part2 = area
            break
        
    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    data = (Path(__file__).parent/"inputs"/"day09.txt").read_text().strip()
    start = time()
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")