from itertools import combinations

def solve(data):

    lines = list(map(lambda line: tuple(map(int, line.split(",")[::-1])), data.split("\n")))
    combos = list(combinations(lines, 2))
    num_points = len(lines)
    
    def rectangle_area(r1, c1, r2, c2):
        return (abs(r1 - r2) + 1) * (abs(c1 - c2) + 1)
        
    # Gives the index of a given point. Inverse of lines. Lines would be index to point
    point_to_index = {p: i for i, p in enumerate(lines)}
    
    row_pad = 1 # Add padding so we can move around the outside of the polygon
    col_pad = 1
    # Compress the grid by only keeping the coordinates that have red tiles
    unique_rows = sorted(set(r for r, c in lines))
    unique_cols = sorted(set(c for r, c in lines))
    row_to_idx = {r: i for i, r in enumerate(unique_rows)}
    col_to_idx = {c: i for i, c in enumerate(unique_cols)}
    compressed_points = [(row_to_idx[r] + row_pad, col_to_idx[c] + col_pad) for r, c in lines]

    # Stores tuples of (area, p1_index, p2_index)
    rectangles = sorted([(
        rectangle_area(*p1, *p2), 
        compressed_points[point_to_index[p1]], 
        compressed_points[point_to_index[p2]]
    ) for p1, p2 in combos], reverse=True)
    
    # Part 1 is the area of the largest rectangle
    part1 = rectangles[0][0]

    max_r = max(r for r, c in compressed_points)
    max_c = max(c for r, c in compressed_points)
    
    rows = max_r + 2 * row_pad # Padding on both bottom and top
    cols = max_c + 2 * col_pad # Padding on both left and right

    # Generate and store the green_tiles (sides) of the polygon
    green_tiles = set()
    red_tiles = set(compressed_points)
    for i in range(len(compressed_points)):
        r1, c1 = compressed_points[i]
        r2, c2 = compressed_points[(i+1)%num_points]
        for c in range(min(c1, c2)+1, max(c1, c2)):
            green_tiles.add((r1, c))
        for r in range(min(r1, r2)+1, max(r1, r2)):
            green_tiles.add((r, c1))

    # Flood fill the outside of the polygon
    q = [(0, 0)] # We know 0, 0 is not inside the polygon because we added padding
    outside = set(q)
    # 2D array where the outside is 0 and the inside of the polygon is 1
    inside = [[1 for _ in range(cols)] for _ in range(rows)]
    while q:
        curr = q.pop(0)
        r, c = curr
        for dr, dc in (1, 0), (-1, 0), (0, 1), (0, -1):
            adj = (r + dr, c + dc)
            ar, ac = adj
            if not (0 <= ar < rows and 0 <= ac < cols):
                continue
            if adj in outside or adj in red_tiles or adj in green_tiles:
                continue
            q.append(adj)
            outside.add(adj)
            inside[ar][ac] = 0

    # Generate a 2D prefix sum using the 'inside' array.
    # Will use this 2D prefix sum to check if a rectangle is fully inside the polygon
    prefix_sum = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            prefix_sum[r][c] = inside[r-1][c-1] + prefix_sum[r-1][c] + prefix_sum[r][c-1] - prefix_sum[r-1][c-1]
            
    def query_prefix_sum(r1, r2, c1, c2): # Assumes (r1, c1) is the top left and (r2, c2) is the bottom right.
        return prefix_sum[r2+1][c2+1] - prefix_sum[r2+1][c1] - prefix_sum[r1][c2+1] + prefix_sum[r1][c1]
    
    # For every rectangle, check if the number of inside tiles (using the prefix sum) is the same as the area of the rectangle
    for area, (r1, c1), (r2, c2) in rectangles:
        if rectangle_area(r1, c1, r2, c2) == query_prefix_sum(*sorted([r1, r2]), *sorted([c1, c2])):
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