from pathlib import Path

def solve():

    from collections import defaultdict

    lines = Path(__file__).with_name('day_09_input.txt').open('r').read().strip().split(" ")
    player_count = int(lines[0])
    last_marble = int(lines[-2])

    marbles = [0]
    curr = 0
    players = defaultdict(int)

    length = 1

    for marble in range(1, last_marble + 1):
        player = marble % player_count

        if marble % 23 == 0:
            curr = (curr - 7) % len(marbles)
            print(f"{int(marble/23)}, {marbles.pop(curr)}")
            #players[player] += marble + marbles.pop(curr)
            length -= 1
        else:
            curr = (curr + 2) % len(marbles)
            marbles.insert(curr, marble)
            length += 1

    part1 = max(players.values())
    part2 = 0

    # part 2: 10 players; last marble is worth 1618 points: 74765078

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")