####### SETUP
with open("day15_input.txt", "r") as file:
    sequence = file.readlines()[0].strip().split(",")

####### PART 1
def customHash(string):
    current_val = 0
    for char in string:
        current_val += ord(char)
        current_val *= 17
        current_val = current_val % 256
    return current_val

total = 0
for string in sequence:
    total += customHash(string)
print(f"PART 1 TOTAL SUM: {total}")

####### PART 2
def talleyLenses(boxes):
    total = 0
    for box in boxes:
        for i, lens in enumerate(boxes[box]):
            total += (box+1) * (i+1) * int(lens.split(" ")[1])
    return total

boxes = {i: [] for i in range(256)}
for string in sequence:
    if "=" in string:
        vals = string.split("=")
        hash_val = customHash(vals[0])

        exists = False
        for i, lens in enumerate(boxes[hash_val]): # if this is too slow, could try using string format and using re to find and replace it
            if vals[0] in lens:
                boxes[hash_val].pop(i)
                boxes[hash_val].insert(i, ' '.join(vals))
                exists = True
        if not exists:
            boxes[hash_val].append(' '.join(vals))

    elif "-" in string:
        hash_val = customHash(string[:-1])

        for i, lens in enumerate(boxes[hash_val]):
            if string[:-1] in lens:
                boxes[hash_val].pop(i)

print(f"PART 2 FOCAL POWER: {talleyLenses(boxes)}")