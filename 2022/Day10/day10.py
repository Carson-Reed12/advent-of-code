####### SETUP 
with open("day10_input.txt", "r") as file:
    instructions = [line.strip() for line in file.readlines()]

####### PART 1
class CRT():
    def __init__(self):
        self.image = []
        self.line = []

    def drawPixel(self, reg_x):
        if len(self.line) in range(reg_x-1, reg_x+2):
            self.line.append("#")
        else:
            self.line.append(".")

        if len(self.line) == 40:
            self.image.append(self.line)
            self.line = []

    def printImage(self):
        for line in self.image:
            print("".join(line))

class CPU():
    def __init__(self):
        self.clock_cycles = 1
        self.reg_x = 1
        self.signal_strengths = {20: 0, 60: 0, 100: 0, 140: 0, 180: 0, 220: 0}
        self.crt = CRT()
    
    def incrementCycle(self):
        self.clock_cycles += 1

        if self.clock_cycles in self.signal_strengths:
            self.signal_strengths[self.clock_cycles] = self.reg_x * self.clock_cycles

    def executeInstruction(self, instruction):
        if instruction == "noop":
            self.crt.drawPixel(self.reg_x)
            self.incrementCycle()
        else:
            val = int(instruction.split()[-1])

            self.crt.drawPixel(self.reg_x)
            self.incrementCycle() # addx takes two cycles. First cycle is pre-add
            self.crt.drawPixel(self.reg_x)
            self.reg_x += val
            self.incrementCycle() # addx takes two cycles. Second cycle is post-add

cpu = CPU()
for instruction in instructions:
    cpu.executeInstruction(instruction)
print(f"PART 1 SIGNAL STRENGTHS: {sum(cpu.signal_strengths.values())}")

####### PART 2
print(f"PART 2 SECRET STRING:")
cpu.crt.printImage()