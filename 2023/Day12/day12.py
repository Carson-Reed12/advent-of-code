import re
import itertools
####### SETUP
with open("day12_input.txt", "r") as file:
    lines = file.readlines()

records = []
for line in lines:
    records.append({"condition": line.split(" ")[0], "groups": [int(group) for group in line.split(" ")[1].strip().split(",")]})

####### PART 1
total = 0
for record in records:
    slots = [index for index in range(len(record["condition"])) if record["condition"][index] == "?"]
    placed_count = sum(record["groups"]) - len([index for index in range(len(record["condition"])) if record["condition"][index] == "#"])

    for trial in itertools.combinations(slots, placed_count):
        test_record = list(record["condition"])
        for slot in trial:
            test_record[slot] = "#"
        new_groups = []
        for m in re.finditer("#+", ''.join(test_record)):
            new_groups.append(len(m.group()))
        if new_groups == record["groups"]:
            total += 1
print(f"PART 1 TOTAL VALID: {total}")
