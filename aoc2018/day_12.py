from pathlib import Path

def solve():

    initial_state, notes  = Path(__file__).with_name('day_12_input.txt').open('r').read().strip().split("\n\n")
    initial_state =  initial_state.split(": ")[1]
    notes = notes.split("\n")
    
    notes = {note.split(" => ")[0]: note.split(" => ")[1] for note in notes}
    
    pots = initial_state
    if pots[0] == "#":
        pots += ".."
    elif pots[1]  == "#":
        pots += "."
    generations = 20
    for _ in range(generations):
        new_pots = ""
        if pots[0] == "#":
            new_pots += ".."
        elif pots[1]  == "#":
            new_pots += "."
        for i in range(len(pots)):
            new_pots += notes.get(pots[i-2:i+3], ".")
            
        if new_pots[-1] == "#":
            new_pots += ".."
        elif new_pots[-2] == "#":
            new_pots += "."
        print(pots)
        
        pots = new_pots
        
    
    part1 = 0
    part2 = 0

    

    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")