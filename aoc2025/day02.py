def solve(data):
    
    line = data.split(",")

    def largest(num_digits):
        return "9" * num_digits
    
    def smallest(num_digits):
        return "1" + "0" * (num_digits - 1)
    
    def invalid_sum(start, end, fragment_lens):
        # Generate invalid ids by checking all possible fragment lengths
        # and testing if the string made up of those fragments duplicated is in the range
        invalids = set()
        for fragment_len in fragment_lens:
            if len(start) % fragment_len != 0:
                continue
            num_fragments = len(start) // fragment_len
            start_fragment = start[:fragment_len]
            end_fragment = end[:fragment_len]
            for fragment in range(int(start_fragment), int(end_fragment) + 1):
                fragment = str(fragment)
                if int(start) <= int(fragment*num_fragments) <= int(end):
                    invalids.add(int(fragment*num_fragments))
        return sum(invalids)
    
    ranges = []
    # Make all start and ends of every range have the same number of digits
    # 50-120 becomes 50-99 and 100-120
    # Uses the fact that all ranges in the input only have at most more 1 digit in the end number than the start number
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
    part1, part2 = solve((Path(__file__).parent/"inputs"/"day02.txt").read_text().strip())
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")