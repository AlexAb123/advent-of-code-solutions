from pathlib import Path
from itertools import permutations
lines = list(map(int, Path(__file__).with_name('07_input.txt').open('r').read().strip().split(",")))

class intcodeComputer():

    def __init__(self, name, lines, inputs):
        self.lines = lines.copy()
        self.index = 0
        self.inputs = inputs
        self.outputs = []
        self.done = False
        self.name = name

    def getModesAndOpcode(self, value):
        modes = [0, 0, 0]
        v = list(map(int, reversed(str(value)[:-2])))
        for i in range(len(v)):
            modes[i] = v[i]
        return (modes, int(str(value)[-2:]))

    def getParameterValue(self, index, mode):
        return self.lines[index] if mode else self.lines[self.lines[index]]
        
    def getOutputs(self):
        self.index = 0
        while self.lines[self.index] != 99:

            modes, opcode = self.getModesAndOpcode(self.lines[self.index])
            p1 = self.getParameterValue(self.index+1, modes[0])

            #if there is a second parameter, get its value depending on its parameterMode
            if opcode != 3 and opcode != 4:
                p2 = self.getParameterValue(self.index+2, modes[1])

            if opcode == 1:
                self.lines[self.lines[self.index+3]] = p1 + p2
                self.index += 4

            elif opcode == 2:
                self.lines[self.lines[self.index+3]] = p1 * p2
                self.index += 4

            elif opcode == 3:
                self.lines[self.lines[self.index+1]] = self.inputs.pop(0)
                self.index += 2

            elif opcode == 4:
                self.outputs.append(p1)
                self.index += 2

            elif opcode == 5:
                if p1 != 0:
                    self.index = p2
                else:
                    self.index += 3

            elif opcode == 6:
                if p1 == 0:
                    self.index = p2
                else:
                    self.index += 3

            elif opcode == 7:
                if p1 < p2:
                    self.lines[self.lines[self.index+3]] = 1
                else:
                    self.lines[self.lines[self.index+3]] = 0
                self.index += 4

            elif opcode == 8:
                if p1 == p2:
                    self.lines[self.lines[self.index+3]] = 1
                else:
                    self.lines[self.lines[self.index+3]] = 0
                self.index += 4

        self.done = True
        return self.outputs

    def runUntilNeedsinput(self):
        temporaryOutputs = []
        while self.lines[self.index] != 99:

            modes, opcode = self.getModesAndOpcode(self.lines[self.index])
            if len(self.inputs) == 0 and opcode == 3:
                break

            p1 = self.getParameterValue(self.index+1, modes[0])
            #if there is a second parameter, get its value depending on its parameterMode
            if opcode != 3 and opcode != 4:
                p2 = self.getParameterValue(self.index+2, modes[1])

            if opcode == 1:
                self.lines[self.lines[self.index+3]] = p1 + p2
                self.index += 4

            elif opcode == 2:
                self.lines[self.lines[self.index+3]] = p1 * p2
                self.index += 4

            elif opcode == 3:
                self.lines[self.lines[self.index+1]] = self.inputs.pop(0)
                self.index += 2

            elif opcode == 4:
                self.index += 2
                self.outputs.append(p1)
                temporaryOutputs.append(p1)

            elif opcode == 5:
                if p1 != 0:
                    self.index = p2
                else:
                    self.index += 3

            elif opcode == 6:
                if p1 == 0:
                    self.index = p2
                else:
                    self.index += 3

            elif opcode == 7:
                if p1 < p2:
                    self.lines[self.lines[self.index+3]] = 1
                else:
                    self.lines[self.lines[self.index+3]] = 0
                self.index += 4

            elif opcode == 8:
                if p1 == p2:
                    self.lines[self.lines[self.index+3]] = 1
                else:
                    self.lines[self.lines[self.index+3]] = 0
                self.index += 4

        if self.lines[self.index] == 99:
            self.done = True

        return temporaryOutputs

def getThrusterOutput(phaseSettings, part1):

    if part1:
        A = intcodeComputer("A", lines, [phaseSettings[0], 0]).getOutputs()[-1]
        B = intcodeComputer("B", lines, [phaseSettings[1], A]).getOutputs()[-1]
        C = intcodeComputer("C", lines, [phaseSettings[2], B]).getOutputs()[-1]
        D = intcodeComputer("D", lines, [phaseSettings[3], C]).getOutputs()[-1]
        E = intcodeComputer("E", lines, [phaseSettings[4], D]).getOutputs()[-1]
        return E
        
    else:
        A = intcodeComputer("A", lines, [phaseSettings[0]])
        B = intcodeComputer("B", lines, [phaseSettings[1]])
        C = intcodeComputer("C", lines, [phaseSettings[2]])
        D = intcodeComputer("D", lines, [phaseSettings[3]])
        E = intcodeComputer("E", lines, [phaseSettings[4]])
        computers = [A, B, C, D, E]
        previousOutput = [0]
        while not E.done:
            for computer in computers:
                if previousOutput != None and previousOutput:
                    for o in previousOutput:
                        computer.inputs.append(o)

                previousOutput = computer.runUntilNeedsinput()
        return E.outputs[-1]

part1Score = 0
for phaseSettings in permutations([0, 1, 2, 3, 4]):
    output = getThrusterOutput(phaseSettings, True)
    part1Score = max(part1Score, output)
print(f"Part 1: {part1Score}")

part2Score = 0
for phaseSettings in permutations([5, 6, 7, 8, 9]):
    output = getThrusterOutput(phaseSettings, False)
    part2Score = max(part2Score, output)
print(f"Part 2: {part2Score}")