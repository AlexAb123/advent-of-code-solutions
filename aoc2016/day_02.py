from pathlib import Path

def solve():

    lines = Path(__file__).with_name('day_02_input.txt').open('r').read().strip().split("\n")

    part2_keypad = (("#", "#", "1", "#", "#"),
                    ("#", "2", "3", "4", "#"),
                    ("5", "6", "7", "8", "9"),
                    ("#", "A", "B", "C", "#"),
                    ("#", "#", "D", "#", "#"))

    part1_move = {"U": lambda x: (max(x[0]-1, 0), x[1]),
            "R": lambda x: (x[0], min(x[1]+1, 2)),
            "D": lambda x: (min(x[0]+1, 2), x[1]),
            "L": lambda x: (x[0], max(x[1]-1, 0))}

    directions = {"U": (-1, 0),
                "R": (0, 1),
                "D": (1, 0),
                "L": (0, -1),}

    part1 = ""
    pos1 = (1, 1)
    part2 = ""
    pos2 = (2, 0)

    for line in lines:
        for c in line:

            pos1 = part1_move[c](pos1)

            new_pos = (pos2[0] + directions[c][0], pos2[1] + directions[c][1])
            pos2 = new_pos if 0 <= new_pos[0] < 5 and 0 <= new_pos[1] < 5 and part2_keypad[new_pos[0]][new_pos[1]] != "#" else pos2
    
        part1 += str(pos1[0] * 3 + pos1[1] + 1)

        part2 += part2_keypad[pos2[0]][pos2[1]]

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")