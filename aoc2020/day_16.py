from pathlib import Path

def solve():
        
    from collections import defaultdict
    import re

    rules, my_ticket, nearby_tickets = Path(__file__).with_name('day_16_input.txt').open('r').read().strip().split("\n\n")
    rules = [(rule.split(":")[0], list(map(int, re.findall(r"\d+", rule)))) for rule in rules.split("\n")]
    rules = {rule[0]: ((rule[1][0], rule[1][1]+1), (rule[1][2], rule[1][3]+1)) for rule in rules}
    my_ticket = list(map(int, my_ticket.split("\n")[1].split(",")))
    nearby_tickets = [tuple(map(int, ticket.split(","))) for ticket in nearby_tickets.split("\n")[1:]]

    part1 = 0
    valid_tickets = set()
    for ticket in nearby_tickets:
        valid = True
        for num in ticket:
            if all(not (r1[0] <= num < r1[1] or r2[0] <= num < r2[1]) for r1, r2 in rules.values()):
                part1 += num
                valid = False
        if valid:
            valid_tickets.add(ticket)

    def get_possible_fields(ticket):
        possible_fields = defaultdict(set)
        for field, (r1, r2) in rules.items():
            for i in range(len(ticket)):
                if (r1[0] <= ticket[i] < r1[1] or r2[0] <= ticket[i] < r2[1]):
                    possible_fields[i].add(field)
        return possible_fields

    def reduce_possible_fields(possible_fields):
        confirmed_fields = set()
        for i, fields in possible_fields.items():
            if len(fields) == 1:
                confirmed_fields.add(list(fields)[0])

        for i, fields in possible_fields.items():
            new_fields = fields.copy()
            for field in fields:
                if len(fields) <= 1:
                    continue
                if field in confirmed_fields:
                    new_fields.remove(field)
            possible_fields[i] = new_fields

        return possible_fields

    possible_fields = defaultdict(lambda: {field for field in rules})
    for ticket in valid_tickets:
        new_possible_fields = get_possible_fields(ticket)
        for i in new_possible_fields:
            possible_fields[i].intersection_update(new_possible_fields[i])

    while any(len(fields) > 1 for fields in possible_fields.values()):
        possible_fields = reduce_possible_fields(possible_fields)

    departure_numbers = set()
    for i, field in possible_fields.items():
        if "departure" in list(field)[0]:
            departure_numbers.add(i)

    part2 = 1
    for i in departure_numbers:
        part2 *= my_ticket[i]

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")