####### SETUP
with open("day8_input.txt", "r") as file:
    board = [list(line.strip()) for line in file.readlines()]

SIZE = len(board)

####### PART 1
def isVisible(coord):
    tree_x = coord[1]
    tree_y = coord[0]
    height = int(board[tree_y][tree_x])

    if tree_x == 0 or tree_y == 0 or tree_x == SIZE-1 or tree_y == SIZE-1:
        return True
    else:
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        current_coord = coord
        visible = True
        for direction in directions:
            current_coord = [current_coord[0] + direction[0], current_coord[1] + direction[1]]
            visible = True
            while 0 <= current_coord[0] < SIZE and 0 <= current_coord[1] < SIZE:
                height_other = int(board[current_coord[0]][current_coord[1]])
                if height_other >= height:
                    current_coord = coord
                    visible = False
                    break
                current_coord = [current_coord[0] + direction[0], current_coord[1] + direction[1]]

            if visible:
                return True
        return False

total = 0
for y, line in enumerate(board):
    for x, height in enumerate(line):
        total += isVisible([y,x])
print(f"PART 1 TOTAL VISIBLE: {total}")

####### PART 2
def scenicScore(coord):
    tree_x = coord[1]
    tree_y = coord[0]
    height = int(board[tree_y][tree_x])

    score = 1
    current_coord = coord
    visible = True
    directions = [[0,1], [0,-1], [1,0], [-1,0]]
    for direction in directions:
        count = 0
        current_coord = [current_coord[0] + direction[0], current_coord[1] + direction[1]]
        while 0 <= current_coord[0] < SIZE and 0 <= current_coord[1] < SIZE:
            count += 1
            height_other = int(board[current_coord[0]][current_coord[1]])
            if height_other >= height:
                current_coord = coord
                break
            else:
                current_coord = [current_coord[0] + direction[0], current_coord[1] + direction[1]]

        score *= count
        current_coord = coord
        
    return score

max_score = 0
for y, line in enumerate(board):
    for x, height in enumerate(line):
        score = scenicScore([y,x])
        max_score = score if score > max_score else max_score
print(f"PART 2 MAX SCORE: {max_score}")