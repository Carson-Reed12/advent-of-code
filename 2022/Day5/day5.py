import re
import copy
####### SETUP
with open("day5_input.txt", "r") as file:
    lines = file.readlines()

box_lines = []
instruction_lines = []
for line in lines:
    if "move" not in line:
        box_lines.append(line)
    else:
        instruction_lines.append(line)

num_stacks = int(box_lines[-2].strip()[-1])
stacks = [[] for _ in range(num_stacks)]
for line in box_lines[:-2]:
    letters = line[1::4]
    for stack_id, letter in enumerate(letters):
        if letter != " ":
            stacks[stack_id].append(letter)

OG_STACKS = copy.deepcopy(stacks)

####### PART 1
def moveCrates(quantity, stack1_id, stack2_id, multi_grab = False):
    global stacks

    moved_crates = stacks[stack1_id][:quantity]
    stacks[stack1_id] = stacks[stack1_id][quantity:]
    stacks[stack2_id] = moved_crates[::-1 if not multi_grab else 1] + stacks[stack2_id]

def getCrateCode(stacks):
    code = ""
    for stack in stacks:
        if stack:
            code += stack[0]
    return code

for instruction in instruction_lines:
    params = re.findall("\d+",instruction)
    quantity, stack1_id, stack2_id = int(params[0]), int(params[1]) - 1, int(params[2]) - 1
    moveCrates(quantity, stack1_id, stack2_id)

print(f"PART 1 CRATE CODE: {getCrateCode(stacks)}")

####### PART 2
stacks = copy.deepcopy(OG_STACKS)

for instruction in instruction_lines:
    params = re.findall("\d+",instruction)
    quantity, stack1_id, stack2_id = int(params[0]), int(params[1]) - 1, int(params[2]) - 1
    moveCrates(quantity, stack1_id, stack2_id, multi_grab=True)

print(f"PART 2 CRATE CODE: {getCrateCode(stacks)}")