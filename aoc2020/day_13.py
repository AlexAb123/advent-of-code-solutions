from pathlib import Path
from math import ceil, lcm
earliest_time, buses = Path(__file__).with_name('day_13_input.txt').open('r').read().strip().split("\n")
earliest_time = int(earliest_time)
buses = buses.split(",")
buses_dict = {}
for i in range(len(buses)):
    if buses[i] == "x":
        continue
    buses_dict[int(buses[i])] = i
possible_times = set()
for bus in buses:
    if bus == "x":
        continue
    bus = int(bus)
    possible_times.add((((ceil(earliest_time / bus) * bus) - earliest_time), bus))

earliest_bus = min(possible_times)
part1 = earliest_bus[0] * earliest_bus[1]
print(f"Part 1: {part1}")

t = 0
while True:
    valid_time = True
    for bus, i in buses_dict.items():
        if buses[i] == "x":
            continue

        if (t + i) % bus != 0:
            valid_time = False
            break

    if valid_time:
        break
    t += int(buses[0])

print(f"Part 2: {t}")
# 100000000000000
# multiple of buses[0]
# multiple of buses[1] + 1
# multiple of buses[2] + 2
# multiple of buses[n] + n