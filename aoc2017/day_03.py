from pathlib import Path


def solve():
    num = int(Path(__file__).with_name('day_03_input.txt').open('r').read().strip())

    def solve_part1(num):
        i = 3
        pos = -1+1j
        length = 2
        while True:

            for _ in range(length): # Left
                i += 1
                pos += -1j
                if i >= num:
                    return int(abs(pos.real)+abs(pos.imag))
            for _ in range(length): # Down
                i += 1
                pos += 1
                if i >= num:
                    return int(abs(pos.real)+abs(pos.imag))
            for _ in range(length+1): # Right
                i += 1
                pos += 1j
                if i >= num:
                    return int(abs(pos.real)+abs(pos.imag))
            length += 2
            for _ in range(length-1): # Up
                i += 1
                pos += -1
                if i >= num:
                    return int(abs(pos.real)+abs(pos.imag))
    part1 = solve_part1(num)


    def solve_part2(num):
        positions = {
            0: 1,
            1j: 1,
        }

        def get_adjs_sum(pos, positions):
            total = 0
            for dr in -1,0,1:
                for dc in -1j,0,1j:
                    if dr == dc == 0:
                        continue
                    if pos+dr+dc in positions.keys():
                        total += positions[pos+dr+dc]
            return total

        pos = -1+1j
        length = 2
        while True:

            for _ in range(length): # Left
                positions[pos] = get_adjs_sum(pos, positions)
                if positions[pos] > num:
                    return positions[pos]
                pos += -1j
            for _ in range(length): # Down
                positions[pos] = get_adjs_sum(pos, positions)
                if positions[pos] > num:
                    return positions[pos]
                pos += 1
            for _ in range(length+1): # Right
                positions[pos] = get_adjs_sum(pos, positions)
                if positions[pos] > num:
                    return positions[pos]
                pos += 1j
            length += 2
            for _ in range(length-1): # Up
                positions[pos] = get_adjs_sum(pos, positions)
                if positions[pos] > num:
                    return positions[pos]
                pos += -1
                
    part2 = solve_part2(num)

    return part1, part2
    
if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")