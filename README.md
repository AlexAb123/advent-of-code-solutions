Skip to content
Navigation Menu
AlexAb123
advent-of-code-solutions

Type / to search
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
advent-of-code-solutions
/
README.md
in
main

Edit

Preview
Indent mode

Spaces
Indent size

4
Line wrap mode

Soft wrap
Editing README.md file contents
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
## Advent of Code Setup Script

A Python utility script to quickly setup [Advent of Code](https://adventofcode.com/) puzzle directories and files.

### Features

- Automatically creates year directory if it doesn't already exist
- Skips files that already exist (safe to re-run)
- Zero-pads day numbers (`day01` instead of `day1`)
- Creates empty input files ready for puzzle input
- Includes execution timing in the template

### Usage

Run `aoc_setup.py`:

```bash
python aoc_setup.py
```

You will be prompted to enter:
1. **Year** - The Advent of Code year (such as `2025`)
2. **Number of days** - How many day files to create (usually `12`)

### What It Creates

For a given year (such as `2025`) and number of days (such as `12`) , the script generates:

```
aoc2025/
├── day01.py
├── day02.py
├── ...
├── day12.py
└── inputs/
    ├── day01.txt
    ├── day02.txt
    ├── ...
    └── day12.txt
```

### Generated File Template

Each `dayXX.py` file comes with a starter template.
Running a `dayXX.py` file directly sets the `input_path` parameter as the path to the correpsonding input file (`inputs/dayXX.txt`).
Implement the `solve` function with `part1` and `part2` as your answers for each part respectively.

```python
# day08.py

def solve(data):

    lines = data.split("\n")

    part1 = part2 = 0

    

    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    start = time()
    part1, part2 = solve((Path(__file__).parent/"inputs"/"day08.txt").read_text().strip())
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")
```


Use Control + Shift + m to toggle the tab key moving focus. Alternatively, use esc then tab to move to the next interactive element on the page.
No file chosen
Attach files by dragging & dropping, selecting or pasting them.
