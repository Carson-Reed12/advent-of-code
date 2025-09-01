import re

####### SETUP
with open("day16_input.txt", "r") as file:
    valve_lines = file.readlines()


####### PART 1
class Valve:
    def __init__(self, line):
        self.id = re.search(r"Valve (\w\w) has", line).group(1)
        self.rate = int(re.search(r"\d+", line).group())
        self.neighbors = re.search(r"valves? (.*)", line).group(1).split(", ")
        self.active = False

    def print(self):
        print(f"{self.id} - Rate: {self.rate}, Neighbors: {self.neighbors}")


valves = [Valve(line) for line in valve_lines]
for valve in valves:
    valve.print()
