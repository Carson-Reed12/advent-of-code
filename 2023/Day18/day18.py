import matplotlib.pyplot as plt
import numpy as np
with open("day18_input.txt", "r") as file:
    lines = file.readlines()

instructions = []
for line in lines:
    instruction = line.strip().split()
    instructions.append({"direction": instruction[0], "distance": int(instruction[1]), "color": instruction[2][1:-1]})

####### PART 1 (adapted from https://github.com/calvinator42000/AoC/blob/main/2023/18_day/1_pt/main.py)
def printBoard(board):
    for line in board:
        print(''.join(line))

def getPoints(instructions):
    points = []
    current_point = [0,0]

    directions = {"R": [0,1], "L": [0,-1], "U": [-1,0], "D": [1,0]}
    for instruction in instructions:
        for _ in range(instruction["distance"]):
            current_point = [current_point[0] + directions[instruction["direction"]][0], current_point[1] + directions[instruction["direction"]][1]]
            points.append(current_point)
    return points

def initializeBoard(points):
    y_min = min([point[0] for point in points])
    y_max = max([point[0] for point in points])
    x_min = min([point[1] for point in points])
    x_max = max([point[1] for point in points])

    y_range = abs(y_min) + abs(y_max) + 1
    x_range = abs(x_min) + abs(x_max) + 1

    board = []
    for _ in range(y_range):
        board.append(list("." * x_range))

    return [abs(y_min), abs(x_min)], board

def createBorder(start, instructions, board):
    current_point = start
    board[start[0]][start[1]] = "#"

    directions = {"R": [0,1], "L": [0,-1], "U": [-1,0], "D": [1,0]}
    for instruction in instructions:
        for _ in range(instruction["distance"]):
            current_point = [current_point[0] + directions[instruction["direction"]][0], current_point[1] + directions[instruction["direction"]][1]]
            board[current_point[0]][current_point[1]] = "#"

def nextDot(board):
    for y, line in enumerate(board):
        for x, char in enumerate(line):
            if char == ".":
                return [y,x]

def getFill(board):
    area = 0
    valid = True
    check_points = [[217,116]]

    directions = {"R": [0,1], "L": [0,-1], "U": [-1,0], "D": [1,0]}
    while check_points:
        current_point = check_points.pop(0)
        board[current_point[0]][current_point[1]] = "#"
        area += 1

        for direction in directions:
            next_point = [current_point[0] + directions[direction][0], current_point[1] + directions[direction][1]]
            if (0 <= next_point[0] < len(board)) and (0 <= next_point[1] < len(board[0])):
                if board[next_point[0]][next_point[1]] == "." and next_point not in check_points:
                    check_points.append(next_point)
            else:
                board[next_point[0]][next_point[1]] = "#"
                valid = False
                break
        if not valid:
            area = 0
            valid = True
            check_points = [nextDot(board)]
    return area

points = getPoints(instructions)
start, board = initializeBoard(points)
createBorder(start, instructions, board)
print(f"PART 1 TOTAL AREA: {len(points) + getFill(board)}")

# hash_points = []
# for y, line in enumerate(board):
#     for x, char in enumerate(line):
#         if char == "#":
#             hash_points.append([y,x])

# plt.scatter(np.array([point[0] for point in hash_points]), np.array([point[1] for point in hash_points]))
# plt.show()


