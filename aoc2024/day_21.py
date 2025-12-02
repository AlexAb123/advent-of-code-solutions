from pathlib import Path

def solve():

    import re
    lines = Path(__file__).with_name('day_21_input.txt').open('r').read().strip().split("\n")

    numeric_positions = {
        '7': 0,
        '8': 1j,
        '9': 2j,
        '4': 1,
        '5': 1+1j,
        '6': 1+2j,
        '1': 2,
        '2': 2+1j,
        '3': 2+2j,
        '0': 3+1j,
        'A': 3+2j,
    }

    directional_positions = {
        '>': 1+2j,
        '<': 1,
        '^': 1j,
        'v': 1+1j,
        'A': 2j,
    }

    cache = {}
    def get_sequences_from_to(curr, target, numeric, sequence="", ):
        if (curr, target, numeric, sequence) in cache:
            return cache[(curr, target, numeric, sequence)]

        if curr == target:
            cache[(curr, target, numeric, sequence)] = {sequence + 'A'} # Add 'A' to the end of every sequence
            return cache[(curr, target, numeric, sequence)]
            
        positions = numeric_positions if numeric else directional_positions

        d = target-curr
        dr = int(d.real)
        dc = int(d.imag)
        sequences = set()

        if dr > 0 and curr + 1 in positions.values(): # Go down
            sequences.update(get_sequences_from_to(curr + 1, target, numeric, sequence + 'v'))
        elif dr < 0 and curr - 1 in positions.values(): # Go up
            sequences.update(get_sequences_from_to(curr - 1, target, numeric, sequence + '^'))
        if dc > 0 and curr + 1j in positions.values(): # Go right
            sequences.update(get_sequences_from_to(curr + 1j, target, numeric, sequence + '>'))
        elif dc < 0 and curr - 1j in positions.values(): # Go left
            sequences.update(get_sequences_from_to(curr - 1j, target, numeric, sequence + '<'))
        cache[(curr, target, numeric, sequence)] = sequences
        return cache[(curr, target, numeric, sequence)]
    
    def get_shortest_sequence_length(sequence, directional_keypads_left, numeric): # Gets the length of the shortest sequence
        if (sequence, directional_keypads_left, numeric) in cache:
            return cache[(sequence, directional_keypads_left, numeric)]
        
        if directional_keypads_left == 0:
            cache[(sequence, directional_keypads_left, numeric)] = len(sequence)
            return cache[(sequence, directional_keypads_left, numeric)]

        positions = numeric_positions if numeric else directional_positions

        shortest_length = 0
        curr = 'A'
        for target in sequence:
            shortest_lengths = set()
            for sequences_from_to in get_sequences_from_to(positions[curr], positions[target], numeric):
                shortest_lengths.add(get_shortest_sequence_length(sequences_from_to, directional_keypads_left - 1, False))

            shortest_length += min(shortest_lengths)
            curr = target
        cache[(sequence, directional_keypads_left, numeric)] = shortest_length
        return cache[(sequence, directional_keypads_left, numeric)]
    
    sequence_cache = {}
    def get_shortest_sequence(sequence, directional_keypads_left, numeric): # Gets the string of the shortest sequence
        if (sequence, directional_keypads_left, numeric) in sequence_cache:
            return sequence_cache[(sequence, directional_keypads_left, numeric)]
        
        if directional_keypads_left == 0:
            sequence_cache[(sequence, directional_keypads_left, numeric)] = sequence
            return sequence_cache[(sequence, directional_keypads_left, numeric)]
        positions = numeric_positions if numeric else directional_positions
        shortest_sequence = ""
        curr = 'A'
        for target in sequence:
            shortest_sequences = set()
            for sequences_from_to in get_sequences_from_to(positions[curr], positions[target], numeric):
                shortest_sequences.add(get_shortest_sequence(sequences_from_to, directional_keypads_left - 1, False))
            shortest_sequence += min(shortest_sequences, key=len)
            curr = target
        sequence_cache[(sequence, directional_keypads_left, numeric)] = shortest_sequence
        return sequence_cache[(sequence, directional_keypads_left, numeric)]

    part1 = 0
    part2 = 0
    for code in lines:
        part1 += get_shortest_sequence_length(code, 3, True) * int(re.findall(r"\d+", code)[0])
        part2 += get_shortest_sequence_length(code, 26, True) * int(re.findall(r"\d+", code)[0])
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")