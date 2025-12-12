from copy import deepcopy
from functools import cache
import numpy as np

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


    def place(region, pos, shape):
        for r in range(len(shape)):
            for c in range(len(shape[0])):
                region[pos[0] + r][pos[1] + c] = shape[r][c]
        return region
        
    @cache
    def can_place(region, shape): # Overlaps region with shape. Region is also 3x3 to allow for efficient memoization

        for r in range(len(shape)):
            for c in range(len(shape[0])):
                if shape[r][c] == "#" and region[r][c] == "#":
                    return False
        return True
        
        
    def can_fit_presents(region, shape_counts):
        if all(count == 0 for count in shape_counts):
            return True
        
        #print(shape_counts)
        
        for i in range(len(shape_counts)):
            if shape_counts[i] != 0:
                shape_idx = i
                break
        
        # PLACE THE NEXT PRESENT in all valid places
        # 
        #print(region, shape_counts)
        #print()
        
        for shape in rotations(shapes[shape_idx]):
            
            for r in range(len(region) - 2):
                for c in range(len(region[0]) - 2):
                    #PLACE SHAPE HERE
                    if can_place(tuple(map(tuple, region[r:r+3, c:c+3])), tuple(map(tuple, shape))):
                        
                        new_shape_counts = shape_counts.copy()
                        new_shape_counts[shape_idx] -= 1
                        
                        new_region = place(region.copy(), (r, c), shape)
                        if can_fit_presents(new_region, new_shape_counts):
                            return True
        return False
        
        
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