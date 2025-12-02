from pathlib import Path

def solve():

    import re
    registers, program = Path(__file__).with_name('day_17_input.txt').open('r').read().strip().split("\n\n")
    registers = registers.split("\n")

    a = int(re.search(r"\d+", registers[0])[0])
    b = int(re.search(r"\d+", registers[1])[0])
    c = int(re.search(r"\d+", registers[2])[0])

    program = list(map(int, re.findall(r"\d+", program)))

    def next_step(a, b, c, i, program):
        
        outputs = []

        instruction = program[i]
        literal_operand = program[i+1]

        combo_operand = literal_operand
        if combo_operand == 4:
            combo_operand = a
        elif combo_operand == 5:
            combo_operand = b
        elif combo_operand == 6:
            combo_operand = c

        if instruction == 0:
            a = a//(2**combo_operand)
            i += 2
        elif instruction == 1:
            b = b ^ literal_operand
            i += 2
        elif instruction == 2:
            b = combo_operand % 8
            i += 2
        elif instruction == 3:
            if a != 0:
                i = literal_operand
            else:
                i += 2
        elif instruction == 4:
            b = b ^ c
            i += 2
        elif instruction == 5:
            outputs.append(combo_operand % 8)
            i += 2
        elif instruction == 6:
            b = a//(2**combo_operand)
            i += 2
        elif instruction == 7:
            c = a//(2**combo_operand)
            i += 2
        return a, b, c, i, outputs

    def run_program(a, b, c, program):
        i = 0
        outputs = []
        while i < len(program):
            a, b, c, i, new_outputs = next_step(a, b, c, i, program)
            outputs += new_outputs
        return outputs

    # Finds a value for the A register that produces next_output
    def find_register_a(next_outputs, program, initial_a=0):
        # If we have outputted all numbers that we needed to, then we have the answer
        if len(next_outputs) == 0:
            return initial_a

        b, c = 0, 0 # Shouldn't matter what these are set to initially

        for da in range(8):
            a = initial_a * 8 + da

            for i in range(0, len(program)-2, 2):
                instruction = program[i]
                literal_operand = program[i+1]
                    
                combo_operand = literal_operand
                if combo_operand == 4:
                    combo_operand = a
                elif combo_operand == 5:
                    combo_operand = b
                elif combo_operand == 6:
                    combo_operand = c
                if instruction == 0:
                    a = a//(2**combo_operand)
                elif instruction == 1:
                    b = b ^ literal_operand
                elif instruction == 2:
                    b = combo_operand % 8
                # Skip instruction 3 - we will return before hitting it anyway
                elif instruction == 4:
                    b = b ^ c
                elif instruction == 5:
                    # If we would output the correct value, then go to the next (previous since we are going in reverse) iteration
                    if combo_operand % 8 == next_outputs[0]:
                        result = find_register_a(next_outputs[1:], program, initial_a * 8 + da)
                        if result != False:
                            return result
                elif instruction == 6:
                    b = a//(2**combo_operand)
                elif instruction == 7:
                    c = a//(2**combo_operand)

        return False

    part1 = ",".join(map(str, run_program(a, b, c, program)))
    part2 = find_register_a(program[::-1], program)
    return part1, part2

if __name__ == "__main__":
    from time import time
    start = time()
    part1, part2 = solve()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {int((time() - start)*100000)/100} ms")