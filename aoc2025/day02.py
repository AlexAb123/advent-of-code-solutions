def solve(input_path):
    
    line = input_path.open('r').read().strip().split(",")

    def largest(num_digits):
        return "9" * num_digits
    
    def smallest(num_digits):
        return "1" + "0" * (num_digits - 1)
    
    def invalid_sum(start, end, shard_lens):
        invalids = set()
        for shard_len in shard_lens:
            if len(start) % shard_len != 0:
                continue
            num_shards = len(start) // shard_len
            start_shard = start[:shard_len]
            end_shard = end[:shard_len]
            for shard in range(int(start_shard), int(end_shard) + 1):
                shard = str(shard)
                if int(start) <= int(shard*num_shards) <= int(end):
                    invalids.add(int(shard*num_shards))
        return sum(invalids)
    
    ranges = []
    for r in line:
        start, end = r.split("-")
        if (len(start) == len(end)):
            ranges.append((start, end))
        else:
            ranges.append((start, largest(len(start))))
            ranges.append((smallest(len(end)), end))

    part1 = 0
    part2 = 0
    for r in ranges:
        start, end = r
        if len(start) % 2 == 0:
            part1 += invalid_sum(start, end, (len(start) // 2,))
        part2 += invalid_sum(start, end, range(1, len(start) // 2 + 1))

    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    start = time()
    part1, part2 = solve(Path(__file__).parent/"inputs"/"day02.txt")
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")