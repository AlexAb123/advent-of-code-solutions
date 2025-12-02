from pathlib import Path
def solve():
    lines = Path(__file__).with_name('day_04_input.txt').open('r').read().strip().split("\n")
    word = "XMAS"
    part1 = 0
    part2 = 0
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == "X":
                for dr in [-1,0,1]:
                    for dc in [-1,0,1]:
                        if dr == 0 and dc == 0:
                            continue
                        if not (0 <= r+3*dr < len(lines) and 0 <= c+3*dc < len(lines)):
                            continue
                        # Check if we have an XMAS in this direction
                        found = True
                        for i in range(1, len(word)):
                            if lines[r+i*dr][c+i*dc] != word[i]:
                                found = False
                                break
                        part1 += found
            # Read the X centered at [r][c]
            if (0 <= r-1 and r+1 < len(lines) and 0 <= r-1 and c+1 < len(lines)) and lines[r][c] == "A":
                m_count = 0
                s_count = 0
                for dr in [-1,1]:
                    for dc in [-1,1]:
                        if lines[r+dr][c+dc] == "M":
                            m_count += 1
                        elif lines[r+dr][c+dc] == "S":
                            s_count += 1
                # If we have 2 M, 2 S, an A at the center (checked earlier), and each set of opposite corners are different letters, then it's an X-MAS
                if m_count == 2 and s_count == 2 and lines[r-1][c-1] != lines[r+1][c+1]:
                    part2 += 1
    return part1, part2
if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")