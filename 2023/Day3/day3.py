import re
####### SETUP
with open("day3_input.txt", "r") as file:
    lines = file.readlines()

board = []
for line in lines:
    board.append(list(line.strip()))

####### PART 1
def checkNumber(index):
    directions = [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1]]
    try:
        while board[index[0]][index[1]] in "0123456789":
            for direction in directions:
                try:
                    check_char = board[index[0] + direction[0]][index[1] + direction[1]]
                    if check_char != "." and check_char not in "0123456789":
                        return True
                except:
                    pass

            index = [index[0], index[1] + 1]
        return False
    except:
        return False

schematic_sum = 0
for i, line in enumerate(lines):
    for m in re.finditer("\d+", line.strip()):
        if checkNumber([i, m.start()]):
            schematic_sum += int(m.group())
print(f"PART 1 SCHEMATIC SUM: {schematic_sum}")

####### PART 2
gear_map = {}
def checkGearNumber(index):
    directions = [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1]]
    try:
        while board[index[0]][index[1]] in "0123456789":
            for direction in directions:
                try:
                    check_char = board[index[0] + direction[0]][index[1] + direction[1]]
                    if check_char == "*":
                        return [index[0] + direction[0], index[1] + direction[1]]
                except:
                    pass

            index = [index[0], index[1] + 1]
        return None
    except:
        return None
    
for i, line in enumerate(lines):
    for m in re.finditer("\d+", line.strip()):
        gear = checkGearNumber([i, m.start()])
        if gear:
            try:
                gear_map[str(gear)].append(int(m.group()))
            except:
                gear_map[str(gear)] = [int(m.group())]

schematic_sum = 0
for gear in gear_map.keys():
    vals = gear_map[gear]
    if len(vals) == 2:
        schematic_sum += vals[0] * vals[1]
print(f"PART 2 SCHEMATIC SUM: {schematic_sum}")