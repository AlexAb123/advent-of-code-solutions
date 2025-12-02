from pathlib import Path
lines = Path(__file__).with_name('day_05_input.txt').open('r').read().strip().split("\n")

seats = []  
for line in lines:
    rowRange = (0, 127)
    for s in line[:-3]:
        if s == "B":
            rowRange = (((rowRange[1]-rowRange[0])//2)+1+rowRange[0], rowRange[1])
        else:
            rowRange = (rowRange[0], rowRange[1] - ((rowRange[1]-rowRange[0])//2)-1)
    colRange = (0, 7)
    for s in line[-3:]:
        if s == "R":
            colRange = (((colRange[1]-colRange[0])//2)+1+colRange[0], colRange[1])
        else:
            colRange = (colRange[0], colRange[1] - ((colRange[1]-colRange[0])//2)-1)
    seats.append(8*rowRange[0] + colRange[0])

seats = sorted(seats)
print(f"Part 1: {seats[-1]}")
for i in range(len(seats)-1):
    if seats[i]+1 != seats[i+1]:
        print(f"Part 2: {seats[i]+1}")
        break