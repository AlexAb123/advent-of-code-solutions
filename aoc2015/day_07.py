from pathlib import Path
import time
lines = Path(__file__).with_name('day_07_input.txt').open('r').read().strip().split("\n")
lines = [line.split(" ") for line in lines]

def bitwise_not(num):
    return (1 << 16) - 1 - num

wires = {}
for line in lines:
    wires[line[-1]] = line

cache = {}
def evaluate_wire(wire, wires):
    if wire in cache:
        return cache[wire]
    
    if wire.isnumeric():
        cache[wire] = int(wire)
        return cache[wire]
    
    line = wires[wire]
    if "AND" in line:
        result = evaluate_wire(line[0], wires) & evaluate_wire(line[2], wires)
    elif "OR" in line:
        result = evaluate_wire(line[0], wires) | evaluate_wire(line[2], wires)
    elif "LSHIFT" in line:
        result = evaluate_wire(line[0], wires) << int(line[2])
    elif "RSHIFT" in line:
        result = evaluate_wire(line[0], wires) >> int(line[2])
    elif "NOT" in line:
        result = bitwise_not(evaluate_wire(line[1], wires))
    else:
        result = evaluate_wire(line[0], wires)
    cache[wire] = result
    return result

start = time.time()
part1 = evaluate_wire("a", wires.copy())
print(f"Part 1: {part1}")

part2_wires = wires.copy()
part2_wires["b"][0] = str(part1)

cache = {}
part2 = evaluate_wire("a", part2_wires)

print(f"Part 2: {part2}")