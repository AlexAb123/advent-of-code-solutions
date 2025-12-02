import math

file = open("AoC_input", "r")
input = file.read().strip().split("\n")

print(input)

for i in range(len(input)):
    input[i] = input[i].split("=")
for i in range(len(input)):
    input[i][1] = input[i][1].split(",")
    input[i][2] = input[i][2].split(":")
    input[i][-2] = input[i][-2].split(",")
for i in range(len(input)):
    input[i] = [(int(input[i][1][0]),int(input[i][2][0])),(int(input[i][3][0]),int(input[i][4]))]
print(input)

def getDist(p1,p2):
    return int(math.fabs(p1[0]-p2[0]) + math.fabs(p1[1]-p2[1]))

num = 2000000

noBeacons = set()
sensors = set()
beacons = set()
for i in input:
    sensors.add(i[0])
    beacons.add(i[1])
for i in input:
    dist = getDist(i[0],i[1])
    if i[0][1]-dist <= num or i[0][1]+dist >= num:
        for x in range(i[0][0]-dist,i[0][0]+dist):
            if getDist(i[0],(x,num)) <= dist:
                if (x,num) not in sensors and (x,num) not in beacons:
                    noBeacons.add((x,num))


print(len(noBeacons))