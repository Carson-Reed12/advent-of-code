import copy
import re
####### SETUP
with open("day14_input.txt", "r") as file:
    lines = file.readlines()
board = [list(line.strip()) for line in lines]

SIZE = len(board)
ORIGINAL_BOARD = copy.deepcopy(board)

def printBoard(board):
    for line in board:
        print(''.join(line))

####### PART 1
def moveRocks(board, direction):
    directions = {"NORTH": [-1, 0], "SOUTH": [1, 0], "EAST": [0, 1], "WEST": [0, -1]}
    cardinal_direction = directions[direction]

    new_board = copy.deepcopy(board)
    for y, line in enumerate(board):
        for x, char in enumerate(line):
            if (0 <= y+cardinal_direction[0] < SIZE) and (0 <= x+cardinal_direction[1] < SIZE):
                if char == "O" and board[y+cardinal_direction[0]][x+cardinal_direction[1]] == ".":
                    new_board[y][x] = "."
                    new_board[y+cardinal_direction[0]][x+cardinal_direction[1]] = "O"
    return new_board

def fullMove(board, direction):
    new_board = moveRocks(board, direction)
    while board != new_board:
        board = copy.deepcopy(new_board)
        new_board = moveRocks(board, direction)
    return board

def calculateLoad(board):
    total = 0
    for y, line in enumerate(board):
        total += (SIZE - y) * len(re.findall("O", ''.join(line)))
    return total

print(f"PART 1 TOTAL LOAD: {calculateLoad(fullMove(board, 'NORTH'))}")

####### PART 2
def cycleBoard(board):
    for direction in ["NORTH", "WEST", "SOUTH", "EAST"]:
        board = fullMove(board, direction)
    return board

def getDiffs(vals):
    diff = vals[1] - vals[0]
    for i in range(len(vals) - 1):
        if (vals[i+1] - vals[i]) != diff:
            return -1
    return diff

vals = {}
boards = []
board = copy.deepcopy(ORIGINAL_BOARD)
for i in range(500):
    board = cycleBoard(board)
    if board not in boards:
        boards.append(board)
    else:
        val = calculateLoad(board)
        if val not in vals:
            vals[val] = [i+1]
        else:
            vals[val].append(i+1)
    print(f"\r{i+1}", end="", flush=True)

for val in vals:
    diff = getDiffs(vals[val])
    if diff != -1:
        start = vals[val][0] - diff

        if ((1000000000 - start)/diff).is_integer: # doesn't really work lol, but print them all out and you'll get the right one
            print(f"\nPART 2 TOTAL LOAD: {val}")
            break
