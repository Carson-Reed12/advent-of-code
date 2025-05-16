import copy
####### SETUP
with open("day19_input.txt", "r") as file:
    lines = file.readlines()

workflows = {}
parts = []
for line in lines:
    if line != "\n":
        if line[0] == "{":
            attributes = line.strip()[1:-1].split(",")
            parts.append({attribute.split("=")[0]: int(attribute.split("=")[1]) for attribute in attributes})
        else:
            workflows[line.split("{")[0]] = line.strip().split("{")[1][:-1].split(",")

####### PART 1
def getRating(part, workflows):
    workflow = "in"
    while workflow != "A" and workflow != "R":
        for condition in workflows[workflow]:
            if ":" in condition and ">" in condition:
                if part[condition[0]] > int(condition.split(">")[1].split(":")[0]):
                    workflow = condition.split(":")[1]
                    break
            elif ":" in condition and "<" in condition:
                if part[condition[0]] < int(condition.split("<")[1].split(":")[0]):
                    workflow = condition.split(":")[1]
                    break
            else:
                workflow = condition
                
    if workflow == "A":
        return sum(part.values())
    else:
        return 0

total_ratings = 0
for part in parts:
    total_ratings += getRating(part, workflows)

print(f"PART 1 TOTAL RATINGS: {total_ratings}")

####### PART 2
def getCombinations(workflows):
    accepted = 0
    queue = ["in"]
    calculate_combinations = lambda a : (a["x"][1] - a["x"][0] + 1) * (a["m"][1] - a["m"][0] + 1) * (a["a"][1] - a["a"][0] + 1) * (a["s"][1] - a["s"][0] + 1)

    combinations = {workflow: {} for workflow in workflows}
    combinations["in"] = {"x": [1,4000], "m": [1,4000], "a": [1,4000], "s": [1,4000]}
    while queue:
        workflow = queue.pop(0)
        remaining_combinations = copy.deepcopy(combinations[workflow])
        for condition in workflows[workflow]:
            if ":" in condition:
                letter = condition[0]
                greater = True if ">" in condition else False
                val = int(condition.split(">")[1].split(":")[0]) if greater else int(condition.split("<")[1].split(":")[0])
                to_workflow = condition.split(":")[1]

                exclusive_eval = (val > remaining_combinations[letter][1]) if greater else (val < remaining_combinations[letter][0])
                inclusive_eval = (val < remaining_combinations[letter][0]) if greater else (val > remaining_combinations[letter][1])
                if exclusive_eval:
                    if to_workflow != "A" and to_workflow != "R":
                        combinations[to_workflow] = {}
                elif inclusive_eval:
                    if to_workflow != "A" and to_workflow != "R":
                        combinations[to_workflow] = remaining_combinations
                        queue.append(to_workflow)
                    elif to_workflow == "A":
                        accepted += calculate_combinations(remaining_combinations)
                    break
                else:
                    send_combinations = copy.deepcopy(remaining_combinations)
                    if greater:
                        send_combinations[letter][0] = val+1
                        remaining_combinations[letter][1] = val
                    else:
                        send_combinations[letter][1] = val-1
                        remaining_combinations[letter][0] = val

                    if to_workflow != "A" and to_workflow != "R":
                        combinations[to_workflow] = send_combinations
                        queue.append(to_workflow)
                    elif to_workflow == "A":
                        accepted += calculate_combinations(send_combinations)
            else:
                to_workflow = condition

                if to_workflow != "A" and to_workflow != "R":
                    combinations[to_workflow] = remaining_combinations
                    queue.append(to_workflow)
                elif to_workflow == "A":
                    accepted += calculate_combinations(remaining_combinations)
    return accepted

print(f"PART 2 TOTAL COMBINATIONS: {getCombinations(workflows)}")