import copy
import math
####### SETUP
with open("day8_input.txt", "r") as file:
    lines = file.readlines()
steps = list(lines[0].strip())

nodes = {}
for line in lines:
    if "=" in line:
        nodes[line.split(" = ")[0]] = {"L": line.split("(")[1][0:3], "R": line.split(", ")[1][0:3]}

####### PART 1
current_node = "AAA"
step_count = 0

while current_node != "ZZZ":
    current_node = nodes[current_node][steps[step_count % len(steps)]]
    step_count += 1
print(f"PART 1 STEP COUNT: {step_count}")

####### PART 2
starting_nodes = []
for node in nodes:
    if node[-1] == "A":
        starting_nodes.append(node)
node_steps = [0 for _ in range(len(starting_nodes))]

step_count = 0
while any(node_step == 0 for node_step in node_steps):
    new_nodes = []
    for node in starting_nodes:
        new_nodes.append(nodes[node][steps[step_count % len(steps)]])
    
    step_count += 1
    starting_nodes = copy.deepcopy(new_nodes)

    for i in range(len(starting_nodes)):
        if starting_nodes[i][-1] == "Z":
            node_steps[i] = step_count
    
lcm = lambda a, b: abs(a * b) // math.gcd(a, b)
total_steps = node_steps[0]
for steps in node_steps:
    if total_steps != steps:
        total_steps = lcm(total_steps, steps)
print(f"PART 2 STEP COUNT: {total_steps}")