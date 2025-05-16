####### SETUP
with open("day4_input.txt", "r") as file:
    pairs = file.readlines()

####### PART 1
def checkSubset(assignment1, assignment2):
    if assignment1[0] >= assignment2[0] and assignment1[1] <= assignment2[1]:
        return 1
    elif assignment2[0] >= assignment1[0] and assignment2[1] <= assignment1[1]:
        return 1
    else:
        return 0
    
total = 0
for pair in pairs:
    assignment1 = [int(val) for val in pair.split(",")[0].split("-")]
    assignment2 = [int(val) for val in pair.split(",")[1].strip().split("-")]
    total += checkSubset(assignment1, assignment2)
print(f"PART 1 TOTAL SUBSETS: {total}")

####### PART 2
def checkOverlap(assignment1, assignment2):
    if assignment2[0] >= assignment1[0] and assignment2[0] <= assignment1[1]:
        return 1
    elif assignment1[0] >= assignment2[0] and assignment1[0] <= assignment2[1]:
        return 1
    else:
        return 0

total = 0
for pair in pairs:
    assignment1 = [int(val) for val in pair.split(",")[0].split("-")]
    assignment2 = [int(val) for val in pair.split(",")[1].strip().split("-")]
    total += checkOverlap(assignment1, assignment2)
print(f"PART 2 TOTAL OVERLAP: {total}")