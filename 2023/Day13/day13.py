import copy
####### SETUP
with open("day13_input.txt", "r") as file:
    lines = file.readlines()

patterns = []
pattern = []
for line in lines:
    if line != "\n":
        pattern.append(list(line.strip()))
    else:
        patterns.append(pattern)
        pattern = []
patterns.append(pattern)

####### PART 1
def printPattern(pattern):
    for y in range(len(pattern)):
        for x in range(len(pattern[0])):
            print(pattern[y][x], end="")
            if x == len(pattern[0]) - 1:
                print()

def checkVertical(pattern, skip = 0):
    reflection = 1
    while reflection < len(pattern[0]):
        if reflection == skip:
            reflection += 1
            continue
        valid = True
        for y in range(len(pattern)):
            for x in range(reflection):
                distance = ((reflection - x) * 2) - 1
                left_char = pattern[y][x]
                try:
                    right_char = pattern[y][x+distance]
                except:
                    continue

                if left_char != right_char:
                    reflection += 1
                    valid = 0
                    break
            if not valid:
                break
        if valid:
            return reflection
    return 0

def checkHorizontal(pattern, skip = 0):
    reflection = 1
    while reflection < len(pattern):
        if reflection == skip:
            reflection += 1
            continue
        valid = True
        for y in range(reflection):
            for x in range(len(pattern[0])):
                distance = ((reflection - y) * 2) - 1
                up_char = pattern[y][x]
                try:
                    down_char = pattern[y+distance][x]
                except:
                    continue

                if up_char != down_char:
                    reflection += 1
                    valid = 0
                    break
            if not valid:
                break
        if valid:
            return reflection
    return 0

total = 0
for pattern in patterns:
    total += checkVertical(pattern) + 100*checkHorizontal(pattern)
print(f"PART 1 TOTAL: {total}")

####### PART 2
def cycleSmudges(pattern):
    toggle = lambda a : "#" if a == "." else "."
    initial_vert = checkVertical(pattern)
    initial_hori = checkHorizontal(pattern)
    for y in range(len(pattern)):
        for x in range(len(pattern[0])):
            pattern[y][x] = toggle(pattern[y][x])
            vertical = checkVertical(pattern, skip=initial_vert)
            horizontal = checkHorizontal(pattern, skip=initial_hori)
            if vertical != 0:
                return vertical
            elif horizontal != 0:
                return 100*horizontal
            else:
                pattern[y][x] = toggle(pattern[y][x])
    return 0

total = 0
for pattern in patterns:
    total += cycleSmudges(pattern)
print(f"PART 2 TOTAL: {total}")