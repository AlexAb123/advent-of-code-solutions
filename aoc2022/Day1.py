file = open("AoC_input", "r")
input = file.read().strip().split("\n")

print(input)

current = 0
lst = []

def findMax(lst):
    max = 0
    for i in lst:
        if i > max:
            max = i
    return max

for elt in input:
    if elt != "":
        current += int(elt)
    else:
        lst.append(current)
        current = 0
lst.append(current)

print(findMax(lst))

max = 0
for i in range(3):
    max = max + findMax(lst)
    lst.remove(findMax(lst))

print(max)
