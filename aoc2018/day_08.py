from pathlib import Path

def solve():

    nums = list(map(int, Path(__file__).with_name('day_08_input.txt').open('r').read().strip().split(" ")))

    part1 = 0
    part2 = 0

    class Node:

        def __init__(self, children, metadata):
            self.children = children
            self.metadata = metadata
        
        def part1_score(self):
            total = 0
            for child in self.children:
                total += child.part1_score()
            return total + sum(self.metadata)
        
        def part2_score(self):
            if len(self.children) == 0:
                return sum(self.metadata)
            total = 0
            for num in self.metadata:
                if num - 1 < len(self.children):
                    total += self.children[num - 1].part2_score()
            return total

        def __repr__(self):
            string = f"{self.metadata}\n"
            for child in self.children:
                for line in child.__repr__().split("\n"):
                    string += "  " + line + "\n"
            return string.strip()
        
    def make_tree(lst):
        child_count, metadata_count = lst.pop(0), lst.pop(0)
        children, metadata = [], []
        for _ in range(child_count):
            children.append(make_tree(lst))
        for _ in range(metadata_count):
            metadata.append(lst.pop(0))
        return Node(children, metadata)

    root = make_tree(nums)
    part1 = root.part1_score()
    part2 = root.part2_score()
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")