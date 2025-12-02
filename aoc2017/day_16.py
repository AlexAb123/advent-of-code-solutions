from pathlib import Path

def solve():

    moves = Path(__file__).with_name('day_16_input.txt').open('r').read().strip().split(",")

    def get_program_by_position(programs, i):
        for program in programs:
            if programs[program] == i:
                return program
        return None

    def dance(program_string):
        programs = {}
        for i, x in enumerate(program_string):
            programs[x] = i
        for move in moves:
            if move[0] == "s":
                for x in programs:
                    programs[x] = (programs[x] + int(move[1:])) % 16

            elif move[0] == "x":
                i1, i2 = map(int, move[1:].split("/"))
                p1 = get_program_by_position(programs, i1)
                p2 = get_program_by_position(programs, i2)
                programs[p1] = i2
                programs[p2] = i1

            elif move[0] == "p":
                p1, p2 = move[1:].split("/")
                programs[p1], programs[p2] = programs[p2], programs[p1]
            
        program_string = "".join(sorted([x for x in "abcdefghijklmnop"], key=lambda x: programs[x]))
        return program_string

    part1 = dance("abcdefghijklmnop")
    program_string = "abcdefghijklmnop"
    cache = {program_string: 0}
    for i in range(1000000000):
        program_string = dance(program_string)
        if program_string not in cache:
            cache[program_string] = i
        else:
            break
    for _ in range(1000000000%(i+1)):
        program_string = dance(program_string)
    part2 = program_string
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")