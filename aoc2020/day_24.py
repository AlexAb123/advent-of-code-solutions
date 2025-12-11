from pathlib import Path
from collections import defaultdict

def solve():

    lines = Path(__file__).with_name('day_24_input.txt').open('r').read().strip().split("\n")


    part1 = 0
    part2 = 0
    
    dirs = {"e": (1, 0, -1), "se": (0, 1, -1), "sw": (-1, 1, 0), "w": (-1, 0, 1), "nw": (0, -1, 1), "ne": (1, -1, 0)}
    
    def adjs(curr):
        for dir in dirs.values():
            yield (curr[0] + dir[0], curr[1] + dir[1], curr[2] + dir[2])
            
    def flip_tile(tile, black_tiles):
        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)
        
    
    black_tiles = set()
    for line in lines:
        curr = (0, 0, 0)
        i = 0
        while i < len(line):
            if i == len(line) - 1 or line[i:i+2] not in dirs:
                dir = dirs[line[i]]
                i += 1
            else:
                dir = dirs[line[i:i+2]]
                i += 2
            curr = (curr[0] + dir[0], curr[1] + dir[1], curr[2] + dir[2])
        flip_tile(curr, black_tiles)
        
    part1 = len(black_tiles)
    for _ in range(100):
        tiles_to_check = set()
        
        for tile in black_tiles:
            tiles_to_check.add(tile)
            for adj in adjs(tile):
                tiles_to_check.add(adj)
                
        new_black_tiles = black_tiles.copy()
        for curr in tiles_to_check:
            
            adjs_count = 0
            
            for adj in adjs(curr):
                adjs_count += adj in black_tiles
            
            if curr in black_tiles:
                if adjs_count == 0 or adjs_count > 2:
                    new_black_tiles.remove(curr)
            else:
                if adjs_count == 2:
                    new_black_tiles.add(curr)
                    
        black_tiles = new_black_tiles
   
    part2 = len(black_tiles)

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")