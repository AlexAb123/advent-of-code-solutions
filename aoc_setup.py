import os
from pathlib import Path

file_template = """def solve(data):

    lines = data.split("\\n")

    part1 = 0
    part2 = 0

    

    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    start = time()
    part1, part2 = solve((Path(__file__).parent/"inputs"/"day{day}.txt").read_text().strip())
    print(f"Part 1: {{part1}}\\nPart 2: {{part2}}")
    print(f"Time Taken: {{(time() - start)*1000:.2f}} ms")"""

files_created = 0

# Create the Year Directory
year = input("Enter year:\n")
days = int(input("Enter number of days:\n"))
path = Path(__file__).with_name("aoc" + year)
if not os.path.exists(path):
    path.mkdir()

for day in (map(str, range(1, days + 1))):

    if len(day) == 1:
        day = "0" + day
    
    # Create the python files
    path = Path(__file__).with_name("aoc" + year) / f"day{day}.py"
    if not os.path.exists(path):
        with path.open("w") as file:
            file.write(file_template.format(day=day))
        print(f"Created file: day{day}.py")
        files_created += 1

    # Create the input files
    inputs_dir = Path(__file__).with_name("aoc" + year) / "inputs"
    inputs_dir.mkdir(exist_ok=True)
    path = inputs_dir / f"day{day}.txt"
    if not os.path.exists(path):
        with path.open("w") as file:
            pass
        print(f"Created file: inputs{os.sep}day{day}.txt")
        files_created += 1

print(f"Created {files_created} file.") if files_created == 1 else print(f"Created {files_created} files.")