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