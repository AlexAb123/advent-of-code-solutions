from pathlib import Path
from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(10000)
rules, messages = Path(__file__).with_name('day_19_input.txt').open('r').read().strip().replace('"', "").split("\n\n")

rules = rules.replace("8: 42", "8: 42 | 42 8")
rules = rules.replace("11: 42 31", "11: 42 31 | 42 11 31")

rules = [rule.split(": ") for rule in rules.split("\n")]
new_rules = {}
for rule in rules:
    new_rules[rule[0]] = set()
    for r in rule[1].split(" | "):
        new_rules[rule[0]].add(tuple(r.split(" ")))

rules = new_rules
messages = messages.split("\n")

max_message_length = len(max(messages, key=len))
print(max_message_length)

@lru_cache
def evaluate_rule(rule, depth):
    if depth >= max_message_length:
        print(rule)
        return {""}
    if not rule.isdigit():
        return {rule}
    
    total_messages = set()
    for sequence in rules[rule]:

        messages = {""}
        for next_rule in sequence:
            next_messages = set()
            for next_message in evaluate_rule(next_rule, depth+1):
                for message in messages:
                    next_messages.add(message + next_message)
            messages = next_messages

        total_messages.update(messages)
    return total_messages
zero = evaluate_rule('0', 0)
part1 = 0
for message in messages:
    if message in zero:
        part1 += 1
print(part1)