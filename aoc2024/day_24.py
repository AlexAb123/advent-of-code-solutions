from pathlib import Path

def solve():

    from collections import defaultdict

    operations = {"AND": lambda x, y: x & y, "OR": lambda x, y: x | y, "XOR": lambda x, y: x ^ y}

    cache = {}
    def evaluate_wire(wire):
        if wire in cache:
            return cache[wire]
        if wire in start_wires:
            cache[wire] = wires[wire]
            return cache[wire]
        wire1, op, wire2 = wires[wire]
        cache[wire] = operations[op](evaluate_wire(wire1), evaluate_wire(wire2))
        return cache[wire]

    wires, gates = Path(__file__).with_name('day_24_input.txt').open('r').read().strip().split("\n\n")
    wires = {wire.split(": ")[0]: int(wire.split(": ")[1]) for wire in wires.split("\n")}
    start_wires = list(wires.keys()).copy()
    gates = [gate.split(" ") for gate in gates.split("\n")]
    z_wires = []
    for gate in gates:
        wires[gate[4]] = tuple(gate[:3])
        if gate[4][0] == "z":
            z_wires.append(gate[4])
    z_wires = list(map(str, (map(evaluate_wire, sorted(z_wires, reverse=True)))))
    part1 = int("".join(z_wires), 2)

    wire_to_ops = defaultdict(set)
    for output_wire, gate in wires.items():
        if output_wire in start_wires:
            continue
        wire1, op, wire2 = gate
        wire_to_ops[wire1].add(op)
        wire_to_ops[wire2].add(op)

    broken_wires = set()
    for output_wire, gate in wires.items():
        if output_wire in start_wires:
            continue
        wire1, op, wire2 = gate
        if output_wire[0] == "z" and op != "XOR" and output_wire != "z45": # Last z (z45) is just the value of the last carry out, so it actually uses an OR instead of XOR
            broken_wires.add(output_wire)
        if op == "AND":
            if not ({"OR"} == wire_to_ops[output_wire] or "x00" in gate or "y00" in gate): # The first adder doesn't have a carry in
                broken_wires.add(output_wire)
        elif op == "XOR":
            if ((wire1[0] != "x" and wire1[0] != "y") and (output_wire[0] != "z")) or ("OR" in wire_to_ops[output_wire]):
                broken_wires.add(output_wire)
    part2 = ",".join(sorted(list(broken_wires)))
    
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")