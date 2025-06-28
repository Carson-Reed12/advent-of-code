####### SETUP 
with open("day14_input.txt", "r") as file:
    lines = file.readlines()

rock_lines = []
for line in lines:
    positions = line.strip().split(" -> ")
    rock_lines.append([[int(pos.split(",")[0]), int(pos.split(",")[1])] for pos in positions])

####### PART 1
def getRange(rock_lines):
    min_x = 99999
    max_x = 0
    max_y = 0

    for line in rock_lines:
        for pos in line:
            if pos[0] < min_x:
                min_x = pos[0]
            if pos[0] > max_x:
                max_x = pos[0]
            if pos[1] > max_y:
                max_y = pos[1]

    return min_x, max_x, max_y

def initializeBoard(rock_lines):
    board = []

    min_x, max_x, max_y = getRange(rock_lines)
    for _ in range(max_y+1):
        board.append(list("." * (max_x - min_x + 3)))

    convertPosX = lambda a : a - min_x + 1

    drawRocks(board, rock_lines, convertPosX)

    return board, convertPosX

def drawRocks(board, rock_lines, convertPosX):
    for line in rock_lines:
        for i in range(len(line)):
            current_pos = line[i]
            try:
                next_pos = line[i+1]
            except:
                break
        
            if current_pos[0] == next_pos[0]:
                for j in range(min(current_pos[1], next_pos[1]), max(current_pos[1], next_pos[1]) + 1):
                    board[j][convertPosX(current_pos[0])] = "#"
            elif current_pos[1] == next_pos[1]:
                for j in range(min(current_pos[0], next_pos[0]), max(current_pos[0], next_pos[0]) + 1):
                    board[current_pos[1]][convertPosX(j)] = "#"

def printBoard(board):
    for line in board:
        print(''.join(line))

class Sand():
    def __init__(self, board, convertPosX):
        self.pos = [convertPosX(500), 0]
        self.drawSand(self.pos, board)

    def fall(self, board):
        size_y = len(board)
        size_x = len(board[0])

        if 0 <= self.pos[1] + 1 < size_y:
            if board[self.pos[1] + 1][self.pos[0]] == ".":
                self.drawSand([self.pos[0], self.pos[1] + 1], board)
                self.pos = [self.pos[0], self.pos[1] + 1]
                return [self.pos[0], self.pos[1] + 1]
            if 0 <= self.pos[0] - 1 < size_x:
                if board[self.pos[1] + 1][self.pos[0] - 1] == ".":
                    self.drawSand([self.pos[0] - 1, self.pos[1] + 1], board)
                    self.pos = [self.pos[0] - 1, self.pos[1] + 1]
                    return [self.pos[0] - 1, self.pos[1] + 1]   
            else:
                board[self.pos[1]][self.pos[0]] = "."
                return "voided"
            if 0 <= self.pos[0] + 1 < size_x:
                if board[self.pos[1] + 1][self.pos[0] + 1] == ".":
                    self.drawSand([self.pos[0] + 1, self.pos[1] + 1], board)
                    self.pos = [self.pos[0] + 1, self.pos[1] + 1]
                    return [self.pos[0] + 1, self.pos[1] + 1]   
            else:
                board[self.pos[1]][self.pos[0]] = "."
                return "voided"
        else:
            board[self.pos[1]][self.pos[0]] = "."
            return "voided"


    def drawSand(self, next_pos, board):
        board[self.pos[1]][self.pos[0]] = "."
        board[next_pos[1]][next_pos[0]] = "o"

def countSand(board):
    total = 0
    for line in board:
        total += sum([1 if char == "o" else 0 for char in line])
    return total

board, convertPosX = initializeBoard(rock_lines)
sand = Sand(board, convertPosX)
last_pos = []
while True:
    new_pos = sand.fall(board)

    if new_pos == "voided":
        break
    elif new_pos != last_pos:
        last_pos = new_pos
    else:
        sand = Sand(board, convertPosX)
print(f"PART 1 SAND COUNT: {countSand(board)}")