import copy
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
