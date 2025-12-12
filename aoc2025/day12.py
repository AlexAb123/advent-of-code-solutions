from copy import deepcopy
from functools import cache
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

def solve(data):

    lines = data

    part1 = part2 = 0

    shapes = [tuple(map(tuple, (line.split("\n")[1:]))) for line in lines[:94].split("\n\n")]
    regions = [line.split(": ") for line in lines[96:].split("\n")]
    
    
    def rotations(shape):
        yield shape
        new_shape = deepcopy(shape)
        for _ in range(3):
            new_shape = [list(row) for row in zip(*new_shape[::-1])]
            yield new_shape
    
    for i in range(len(regions)):
        regions[i][0] = list(map(int, regions[i][0].split("x")))
        regions[i][1] = list(map(int, regions[i][1].split(" ")))

    @cache
    def place(region, shape):
        new_region = [["." for _ in range(len(shape))] for _ in range(len(shape[0]))]
        for r in range(len(shape)):
            for c in range(len(shape[0])):
                if shape[r][c] == "#" and region[r][c] == "#":
                    return None
                new_region[r][c] = shape[r][c]
        return new_region
        
    def can_place(region, shape): # Overlaps region with shape. Region is also 3x3 to allow for efficient memoization

        for r in range(len(shape)):
            for c in range(len(shape[0])):
                if shape[r][c] == "#" and region[r][c] == "#":
                    return False
        return True
    
    shape_spaces = [0 for _ in range(len(shapes))]
    for i in range(len(shapes)):
        count = 0
        for r in range(len(shapes[i])):
            for c in range(len(shapes[i][0])):
                if shapes[i][r][c] == "#":
                    count += 1
        shape_spaces[i] = count
    print(shape_spaces)
    cache_ = {}
    def can_fit_presents(region, shape_counts):
        key = (tuple(map(tuple, region)), tuple(shape_counts))
        if key in cache_:
            return cache_[key]
        if all(count == 0 for count in shape_counts):
            cache_[key] = True
            return True
            
        total_space_needed = 0
        for i, count in enumerate(shape_counts):
            total_space_needed += shape_spaces[i] * count
        total_space_left = 0
        for r in range(len(region)):
            for c in range(len(region[0])):
                if region[r][c] == ".":
                    total_space_left += 1
        if total_space_left < total_space_needed:
            cache_[key] = False
            return False
        print(total_space_left, total_space_needed)
        #print(shape_counts)
        
        for i in range(len(shape_counts)):
            if shape_counts[i] != 0:
                shape_idx = i
                break
        
        # PLACE THE NEXT PRESENT in all valid places
        # 
        print(region, shape_counts)
        # 
        

        for shape in rotations(shapes[shape_idx]):
            
            for r in range(len(region) - 2):
                for c in range(len(region[0]) - 2):
                    #PLACE SHAPE HERE
                    
                    if not can_place(tuple(map(tuple, region[r:r+3, c:c+3])), tuple(map(tuple, shape))):
                       continue 
                    new_region = region.copy()
                    new_region[r:r+3, c:c+3] = place(tuple(map(tuple, new_region[r:r+3, c:c+3])), tuple(map(tuple, shape)))
                    #print("can place")
                    new_shape_counts = shape_counts.copy()
                    new_shape_counts[shape_idx] -= 1
                    if can_fit_presents(new_region, new_shape_counts):
                        cache_[key] = True
                        return True
        cache_[key] = False
        return False

    # Can go down the list in and do ones with duplicate dimensions that are stricly harder (more of a certain type of present).
    # If the strictly harder one is possible, then so is the strictly easier one.

    part1 = 0
    for dimensions, shape_counts in regions:
        region = np.array([["." for _ in range(dimensions[0])] for _ in range(dimensions[1])])
        part1 += can_fit_presents(region, shape_counts)
        print(part1)
        
    

    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    data = (Path(__file__).parent/"inputs"/"day12.txt").read_text().strip()
    start = time()
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")