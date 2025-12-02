from pathlib import Path
lines = list(map(int, Path(__file__).with_name('05_input.txt').open('r').read().strip().split(",")))

class intcodeComputer():

    def __init__(self, lines, inputs):
        self.lines = lines.copy()
        self.index = 0
        self.inputs = inputs
        self.outputs = []

    def getModesAndOpcode(self, value):
        modes = [0, 0, 0]
        v = list(map(int, reversed(str(value)[:-2])))
        for i in range(len(v)):
            modes[i] = v[i]
        return (modes, int(str(value)[-2:]))

    def getParameterValue(self, index, mode):
        return self.lines[index] if mode else self.lines[self.lines[index]]
        
    def getOutputs(self):
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

        return self.outputs

print(f'Part 1: {intcodeComputer(lines, [1]).getOutputs()[-1]}')
print(f'Part 2: {intcodeComputer(lines, [5]).getOutputs()[-1]}')
