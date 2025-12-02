from pathlib import Path

def solve():
    p1, p2 = Path(__file__).with_name('day_21_input.txt').open('r').read().strip().split("\n")
    p1 = int(p1.split(": ")[-1])
    p2 = int(p2.split(": ")[-1])

    starting_positions = [p1, p2]
    scores = [0, 0]
    positions = starting_positions.copy()
    rolls = 0
    dice = 0
    turn = 0
    while True:

        forward = 0
        for _ in range(3):
            rolls += 1
            dice += 1

            forward += dice

            if dice > 100:
                dice = 1
        positions[turn] += forward
        while positions[turn] > 10:
            positions[turn] -= 10
        scores[turn] += positions[turn]
        if scores[turn] >= 1000:
            break
        turn += 1
        turn %= 2

    part1 = scores[(turn+1)%2]*rolls


    cache = {}
    def simulate_game_part2(positions, scores=[0,0], turn=0):

        if (tuple(positions), tuple(scores), turn) in cache:
            return cache[(tuple(positions), tuple(scores), turn)]

        if max(scores) >= 21:
            ans = 1j if turn == 0 else 1
            cache[(tuple(positions), tuple(scores), turn)] = ans
            return ans
        
        wins = 0
        
        for i in 1,2,3:
            for j in 1,2,3:
                for k in 1,2,3:

                    forward = i + j + k
                    new_positions = positions.copy()
                    new_scores = scores.copy()
                    new_positions[turn] += forward
                    if new_positions[turn] > 10:
                        new_positions[turn] -= 10
                    new_scores[turn] += new_positions[turn]

                    wins += simulate_game_part2(new_positions, new_scores, (turn + 1) % 2)

        cache[(tuple(positions), tuple(scores), turn)] = wins
        return wins
        
    wins = [0, 0]
    wins_complex = simulate_game_part2(starting_positions)
    wins[0] = int(wins_complex.real)
    wins[1] = int(wins_complex.imag)
    part2 = max(wins)

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")