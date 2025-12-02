from pathlib import Path

def solve():

    lines = Path(__file__).with_name('day_10_input.txt').open('r').read().strip().split("\n")

    opens = {'(', '[', '{', '<'}
    closes = {')', ']', '}', '>'}
    close_to_open = {')': '(', ']': '[', '}': '{', '>': '<'}
    open_to_close = {'(': ')', '[': ']', '{': '}', '<': '>'}

    def find_corrupt_characters(line, currently_open):

        if len(line) == 0:
            return [], currently_open

        corrupt_characters = []

        # If it's an opener, add it to currently_open
        if line[0] in opens:
            currently_open.append(line[0])
        elif line[0] in closes:

            # If we find the right closer for the most recent opener, it's a valid chunk
            if currently_open[-1] == close_to_open[line[0]]:
                currently_open.pop(-1)

            # If it's not the right closer, then it's corrupt
            else:
                corrupt_characters.append(line[0])
        
        corrupt_characters += find_corrupt_characters(line[1:], currently_open)[0]
        return corrupt_characters, currently_open
    
    points_part1 = {
            ")": 3,
            "]": 57,
            "}": 1197,
            ">": 25137
    }
    points_part2 = {
            ")": 1,
            "]": 2,
            "}": 3,
            ">": 4
    }
    part1 = 0
    autocomplete_scores = []
    for line in lines:

        corrupt_characters, not_closed = find_corrupt_characters(line, [])

        if not corrupt_characters:
            autocomplete_score = 0
            for c in map(lambda x: open_to_close[x], reversed(not_closed)):
                autocomplete_score *= 5
                autocomplete_score += points_part2[c]
            autocomplete_scores.append(autocomplete_score)

        else:
            part1 += points_part1[corrupt_characters[0]]

    autocomplete_scores = sorted(autocomplete_scores)
    part2 = autocomplete_scores[len(autocomplete_scores)//2]

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")