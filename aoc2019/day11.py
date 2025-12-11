from copy import deepcopy
def solve(data):

    lines = data.split("\n")

    part1 = part2 = 0

    pos = []
    vel = []
    for line in lines:
        x, y, z =  line.split(",")
        x = int(x[3:])
        y = int(y[3:])
        z = int(z[3:-1])
        pos.append([x, y, z])
        vel.append([0, 0, 0])
        
    step = 0
    seen_pos = set()
    seen_vel = set()
    while True:
        
        # Apply gravity
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                for axis in range(3):
                    if pos[i][axis] == pos[j][axis]:
                        continue
                    if pos[i][axis] < pos[j][axis]:
                        vel[i][axis] += 1
                        vel[j][axis] -= 1
                    else:
                        vel[i][axis] -= 1
                        vel[j][axis] += 1
                        
        # Apply velocity
        for i in range(len(pos)):
            for axis in range(3):
                if vel[i][axis] == 0:
                    continue
                pos[i][axis] += vel[i][axis]
        
        print(pos, vel)
        if step % 10000 == 0:
            print(step)
        
        if tuple(map(tuple, pos)) in seen_pos and tuple(map(tuple, vel)) in seen_vel:
            part2 = step
            break
        
        if step == 999:
            part1 = 0
            for i in range(len(pos)):
                pot = 0
                kin = 0
                for axis in range(3):
                    pot += abs(pos[i][axis])
                    kin += abs(vel[i][axis])
                part1 += pot * kin
        step += 1
        seen_pos.add(tuple(map(tuple, pos)))
        seen_vel.add(tuple(map(tuple, vel)))
        
    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    data = (Path(__file__).parent/"inputs"/"day11.txt").read_text().strip()
    start = time()
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")