import itertools
import math
from Library import *

file = open("AoC_input", "r")
input = file.read().strip().split("\n")

def reverseStr(s):
    n = ""
    for i in range(len(s)-1,-1,-1):
        n = n + s[i]
    return n

def toDec(s):
    temp = 0
    for j in range(len(s)):
        if s[j] == "=":
            temp = temp + (-2 * (math.pow(5, j)))
        elif s[j] == "-":
            temp = temp + (-1 * (math.pow(5, j)))

        elif s[j] == "0":
            temp = temp + (0 * (math.pow(5, j)))

        elif s[j] == "1":
            temp = temp + (1 * (math.pow(5, j)))

        elif s[j] == "2":
            temp = temp + (2 * (math.pow(5, j)))
    return temp

totals = []
temp = 0
for i in input:
    s = reverseStr(i)
    totals.append(toDec(s))

m = 0
for i in totals:
    m = m + i
m = int(m)

num = m
new = ""

while num != 0:

    if num%5 == 0:
        new = "0" + new

    elif num%5 == 1:
        new = "1" + new

    elif num%5 == 2:
        new = "2" + new

    elif num%5 == 3:
        new = "=" + new
        num = num + 5

    elif num%5 == 4:
        new = "-" + new
        num = num + 5

    num = num//5

print(new)

