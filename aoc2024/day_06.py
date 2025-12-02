from pathlib import Path
def solve():
    import bisect
    from collections import defaultdict
    # HAS CYCLE TAKES ABOUT 200 ms, FIND NEXT OBSTRUCTION TAKES UP 90 OF THOSE
    def has_cycle(pos, direction, obstructions_rows, obstructions_columns, seen_states):
        while True:
            # If we have been in this position and direction before, we have found a cycle
            if (pos, direction) in seen_states:
                return True
            seen_states.add((pos, direction))

            # If there is an obstruction in front of us, go to it and turn, if not, there isn't a cycle
            pos, direction = find_next_obstruction(pos, direction, obstructions_rows[pos[0]], obstructions_columns[pos[1]])
            if not pos:
                return False

    lines = Path(__file__).with_name('day_06_input.txt').open('r').read().strip().split("\n")

    obstructions = set()
    start = None

    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == "^":
                start = (r,c)
            elif lines[r][c] == "#":
                obstructions.add((r,c))

    right_turns = {(-1,0): (0,1),
                (0,1): (1,0),
                (1,0): (0,-1),
                (0,-1): (-1,0)}
    direction = (-1,0)

    pos = start
    patrol_path = set()
    seen_states = set()
    part2 = 0

    obstructions_rows = defaultdict(list)
    obstructions_columns = defaultdict(list)

    for obstruction in obstructions:
        bisect.insort(obstructions_rows[obstruction[0]], obstruction[1])
        bisect.insort(obstructions_columns[obstruction[1]], obstruction[0])
    
    cache = {}
    def find_next_obstruction(pos, direction, obstructions_row, obstructions_column):
        if (pos, direction, tuple(obstructions_row), tuple(obstructions_column)) in cache:
            return cache[(pos, direction, tuple(obstructions_row), tuple(obstructions_column))]
        match direction:

            case (-1,0):
                i = bisect.bisect_left(obstructions_column, pos[0])
                if i > 0:
                    value = ((obstructions_column[i - 1] - direction[0], pos[1] - direction[1]), right_turns[direction])
                    cache[(pos, direction, tuple(obstructions_row), tuple(obstructions_column))] = value
                    return value

            case (0, 1):
                i = bisect.bisect_right(obstructions_row, pos[1])
                if i < len(obstructions_row):
                    value = ((pos[0] - direction[0], obstructions_row[i] - direction[1]), right_turns[direction])
                    cache[(pos, direction, tuple(obstructions_row), tuple(obstructions_column))] = value
                    return value

            case (1, 0):
                i = bisect.bisect_right(obstructions_column, pos[0])
                if i < len(obstructions_column):
                    value = ((obstructions_column[i] - direction[0], pos[1] - direction[1]), right_turns[direction])
                    cache[(pos, direction, tuple(obstructions_row), tuple(obstructions_column))] = value
                    return value

            case (0, -1):
                i = bisect.bisect_left(obstructions_row, pos[1])
                if i > 0:
                    value = ((pos[0] - direction[0], obstructions_row[i - 1] - direction[1]), right_turns[direction])
                    cache[(pos, direction, tuple(obstructions_row), tuple(obstructions_column))] = value
                    return value
        return False, False    
        
    while True:

        patrol_path.add(pos)
        seen_states.add((pos, direction))

        next_pos = (pos[0] + direction[0], pos[1] + direction[1])

        # If there is an obstruction in front of us, turn
        if next_pos in obstructions:
            direction = right_turns[direction]

        else:


            # If we haven't been to next_pos before, then check if adding an obstruction there will cause a cycle
            # Have to check if we have been to next_pos before because if we have and we add an obstruction, then we would block our path
            # meaning we would never have been able to get to the position we are in
            if next_pos not in patrol_path:

                new_obstructions_rows = obstructions_rows.copy()
                new_obstructions_rows[next_pos[0]] = obstructions_rows[next_pos[0]].copy()
                bisect.insort(new_obstructions_rows[next_pos[0]], next_pos[1])

                new_obstructions_columns = obstructions_columns.copy()
                new_obstructions_columns[next_pos[1]] = obstructions_columns[next_pos[1]].copy()
                bisect.insort(new_obstructions_columns[next_pos[1]], next_pos[0])

                part2 += has_cycle(pos, right_turns[direction], new_obstructions_rows, new_obstructions_columns, seen_states.copy())
            pos = next_pos

            # If we go out of bounds, end the loop
            if not (0 <= pos[0] < len(lines) and 0 <= pos[1] < len(lines[0])):
                break
    part1 = len(patrol_path)
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")