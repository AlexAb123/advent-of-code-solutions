import math
import itertools as it
from Library import *
import sympy

file = open('AoC_input', 'r')
input = file.read().strip().split("\n")
monkeys = {}
for i in input:
    name = i.split(":")[0]
    op = i.split(": ")[1]
    if op.isnumeric():
        op = int(op)
    monkeys[name] = op

def setNum(name):
    if name == "humn":
        return sympy.Symbol("x")
    if isinstance(monkeys[name],str):
        op = monkeys[name].split()[1]
        m1 = monkeys[name].split()[0]
        m2 = monkeys[name].split()[2]

        if op == "+":
            monkeys[name] = setNum(m1) + setNum(m2)
        if op == "-":
            monkeys[name] = setNum(m1) - setNum(m2)
        if op == "*":
            monkeys[name] = setNum(m1) * setNum(m2)
        if op == "/":
            monkeys[name] = setNum(m1) / setNum(m2)

    return monkeys[name]

eq1 = monkeys["root"].split()[0]
eq2 = monkeys["root"].split()[2]

for i in monkeys:
    monkeys[i] = setNum(i)
print(monkeys)

print(sympy.solve(monkeys[eq1]-monkeys[eq2])[0])

#PART 2 BRUTE FORCE - TOO SLOW
'''class Monkey():
    def __init__(self,name=None,op=None):
        self.name = name
        self.op = op
    def getName(self):
        return self.name
    def getOp(self):
        return self.op
    def setOp(self,op):
        self.op = op
    def __repr__(self):
        return (f"{self.name}, {self.op}")


file = open('AoC_input', 'r')
input = file.read().strip().split("\n")
monkeys = []
for i in input:
    name = i.split(":")[0]
    op = i.split(": ")[1]
    if op.isnumeric():
        op = int(op)
    monkeys.append(Monkey(name,op))

def findMon(name):
    for mon in monkeys:
        if mon.getName() == name:
            return mon

def findNum(mon):
    if isinstance(mon.getOp(),int):
        return mon.getOp()
    ope = mon.getOp().split()[1]
    n1 = mon.getOp().split()[0]
    n2 = mon.getOp().split()[2]

    if ope == "+":
        return findNum(findMon(n1)) + findNum(findMon(n2))
    if ope == "-":
        return findNum(findMon(n1)) - findNum(findMon(n2))
    if ope == "*":
        return findNum(findMon(n1)) * findNum(findMon(n2))
    if ope == "/":
        return findNum(findMon(n1)) / findNum(findMon(n2))


equal1 = findMon(findMon("root").getOp().split()[0])
equal2 = findMon(findMon("root").getOp().split()[2])
print(equal2,equal1)
i = 0
print(findNum(equal1))
print(findNum(equal2))
while findNum(equal1) != findNum(equal2):
    findMon("humn").setOp(i)
    i = i + 1
    if i%100 == 0:
        print(i)
print(i-1)'''
#PART 1
'''import math
import itertools as it
from Library import *

class Monkey():
    def __init__(self,name=None,op=None):
        self.name = name
        self.op = op
    def getName(self):
        return self.name
    def getOp(self):
        return self.op
    def __repr__(self):
        return (f"{self.name}, {self.op}")

    def findNumber(self):
        pass


file = open('AoC_input', 'r')
input = file.read().strip().split("\n")
monkeys = []
for i in input:
    name = i.split(":")[0]
    op = i.split(": ")[1]
    if op.isnumeric():
        op = int(op)
    monkeys.append(Monkey(name,op))

def findMon(name):
    for mon in monkeys:
        if mon.getName() == name:
            return mon

def findNum(mon):
    if isinstance(mon.getOp(),int):
        return mon.getOp()
    ope = mon.getOp().split()[1]
    n1 = mon.getOp().split()[0]
    n2 = mon.getOp().split()[2]

    if ope == "+":
        return findNum(findMon(n1)) + findNum(findMon(n2))
    if ope == "-":
        return findNum(findMon(n1)) - findNum(findMon(n2))
    if ope == "*":
        return findNum(findMon(n1)) * findNum(findMon(n2))
    if ope == "/":
        return findNum(findMon(n1)) / findNum(findMon(n2))

print(findNum(findMon("root")))
'''