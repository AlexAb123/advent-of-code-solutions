from pathlib import Path

def solve():
        
    from collections import defaultdict

    lines = list(map(int, Path(__file__).with_name('day_22_input.txt').open('r').read().strip().split("\n")))

    def evolve_number(num):
        num = (num ^ (num * 64)) % 16777216
        num = (num ^ (num // 32)) % 16777216
        num = (num ^ (num * 2048)) % 16777216
        return num

    def get_secret_numbers(num, evolutions):
        secret_numbers = [num]
        for _ in range(evolutions):
            secret_numbers.append(evolve_number(secret_numbers[-1]))
        return tuple(secret_numbers)

    all_secret_numbers = [get_secret_numbers(num, 2000) for num in lines]

    part1 = sum(secret_numbers[-1] for secret_numbers in all_secret_numbers)

    sequence_profits = defaultdict(int)
    for i in range(len(lines)):
        secret_numbers = all_secret_numbers[i]
        differences = []
        seen_sequences = set()
        for j in range(1, len(secret_numbers)):
            differences.append((secret_numbers[j]%10) - (secret_numbers[j-1]%10))
            if j >= 4:
                sequence = tuple(differences[j-4:j])
                if sequence not in seen_sequences: # Only use the first occurence of the sequence
                    sequence_profits[sequence] += secret_numbers[j]%10
                    seen_sequences.add(sequence)

    part2 = max(sequence_profits.values())

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")