####### SETUP 
with open("day9_input.txt", "r") as file:
    moves = file.readlines()

####### PART 1
class Knot:
    def __init__(self):
        self.head = [0,0]
        self.tail = [0,0]
        self.tail_positions = [[0,0]]

    def move(self, direction):
        directions = {"R": [0,1], "L": [0,-1], "U": [-1,0], "D": [1,0], "UR": [-1,1], "UL": [-1,-1], "DR": [1,1], "DL": [1,-1]}
        opp_dir = {"R": "L", "L": "R", "U": "D", "D": "U"}
        lat_dir = {"R": ["U", "D"], "L": ["U", "D"], "U": ["R", "L"], "D": ["R", "L"]}

        if self.tail != self.head:
            if direction in "RLUD":
                if self.tail == [self.head[0] + directions[opp_dir[direction]][0], self.head[1] + directions[opp_dir[direction]][1]]:
                    self.tail = [self.tail[0] + directions[direction][0], self.tail[1] + directions[direction][1]]
                elif self.tail == [self.head[0] + directions[opp_dir[direction]][0] + directions[lat_dir[direction][0]][0], self.head[1] + directions[opp_dir[direction]][1] + directions[lat_dir[direction][0]][1]]:
                    self.tail = [self.tail[0] + directions[direction][0] + directions[lat_dir[direction][1]][0], self.tail[1] + directions[direction][1] + directions[lat_dir[direction][1]][1]]
                elif self.tail == [self.head[0] + directions[opp_dir[direction]][0] + directions[lat_dir[direction][1]][0], self.head[1] + directions[opp_dir[direction]][1] + directions[lat_dir[direction][1]][1]]:
                    self.tail = [self.tail[0] + directions[direction][0] + directions[lat_dir[direction][0]][0], self.tail[1] + directions[direction][1] + directions[lat_dir[direction][0]][1]]
            else:
                if direction == "UR":
                    if self.tail == [self.head[0], self.head[1]-1] or self.tail == [self.head[0]+1, self.head[1]] or self.tail == [self.head[0]+1, self.head[1]-1]:
                        self.tail = [self.tail[0] - 1, self.tail[1] + 1]
                    elif self.tail == [self.head[0]-1, self.head[1]-1]:
                        self.tail = [self.tail[0], self.tail[1] + 1]
                    elif self.tail == [self.head[0]+1, self.head[1]+1]:
                        self.tail = [self.tail[0]-1, self.tail[1]]

                if direction == "UL":
                    if self.tail == [self.head[0], self.head[1]+1] or self.tail == [self.head[0]+1, self.head[1]] or self.tail == [self.head[0]+1, self.head[1]+1]:
                        self.tail = [self.tail[0] - 1, self.tail[1] - 1]
                    elif self.tail == [self.head[0]-1, self.head[1]+1]:
                        self.tail = [self.tail[0], self.tail[1] - 1]
                    elif self.tail == [self.head[0]+1, self.head[1]-1]:
                        self.tail = [self.tail[0]-1, self.tail[1]]  

                if direction == "DR":
                    if self.tail == [self.head[0], self.head[1]-1] or self.tail == [self.head[0]-1, self.head[1]-1] or self.tail == [self.head[0]-1, self.head[1]]:
                        self.tail = [self.tail[0] + 1, self.tail[1] + 1]
                    elif self.tail == [self.head[0]+1, self.head[1]-1]:
                        self.tail = [self.tail[0], self.tail[1]+1]
                    elif self.tail == [self.head[0]-1, self.head[1]+1]:
                        self.tail = [self.tail[0]+1, self.tail[1]]

                if direction == "DL":
                    if self.tail == [self.head[0]-1, self.head[1]] or self.tail == [self.head[0]-1, self.head[1]+1] or self.tail == [self.head[0], self.head[1]+1]:
                        self.tail = [self.tail[0] + 1, self.tail[1] - 1]
                    elif self.tail == [self.head[0]-1, self.head[1]-1]:
                        self.tail = [self.tail[0]+1, self.tail[1]]
                    elif self.tail == [self.head[0]+1, self.head[1]+1]:
                        self.tail = [self.tail[0], self.tail[1]-1]


        if self.tail not in self.tail_positions:
            self.tail_positions.append(self.tail)
        self.head = [self.head[0] + directions[direction][0], self.head[1] + directions[direction][1]]

knot = Knot()
for move in moves:
    direction = move.split()[0]
    num_moves = int(move.split()[-1])
    for _ in range(num_moves):
        knot.move(direction)
print(f"PART 1 TAIL LOCATIONS: {len(knot.tail_positions)}")

####### PART 2
class Rope:
    def __init__(self, num_knots):
        self.knots = [Knot() for _ in range(num_knots)]

    def move(self, direction):
        direction_map = {"[0, -1]": "R", "[0, 1]": "L", "[1, 0]": "U", "[-1, 0]": "D", "[1, -1]": "UR", "[1, 1]": "UL", "[-1, -1]": "DR", "[-1, 1]": "DL", "[0, 0]": None}
        knot_id = 0

        current_tail = self.knots[knot_id].tail
        self.knots[knot_id].move(direction)
        new_dir = direction_map[str([current_tail[0] - self.knots[knot_id].tail[0], current_tail[1] - self.knots[knot_id].tail[1]])]
        print(new_dir)

        while new_dir and knot_id < len(self.knots)-1:
            knot_id += 1

            current_tail = self.knots[knot_id].tail
            self.knots[knot_id].move(new_dir)
            new_dir = direction_map[str([current_tail[0] - self.knots[knot_id].tail[0], current_tail[1] - self.knots[knot_id].tail[1]])]
            # print(f"{knot_id} NEW DIR: {new_dir}")

def initializeBoard(size):
    board = []
    for _ in range(size):
        board.append(list("."*size))
    return board

def resetBoard(board):
    for y, line in enumerate(board):
        for x, char in enumerate(line):
            if char == "#":
                board[y][x] = "."

def printBoard(rope, board):
    resetBoard(board)
    for knot in rope.knots:
        head = knot.head
        board[head[0] + len(board)//2][head[1] + len(board)//2] = "#"

    board[rope.knots[-2].tail[0] + len(board)//2][rope.knots[-2].tail[1] + len(board)//2] = "@"
    
    for line in board:
        print("".join(line))

def printStats(rope):
    for i in range(len(rope.knots)):
        print(f"Knot {i} - Head: {rope.knots[i].head} - Tail: {rope.knots[i].tail}")

rope = Rope(10)
board = initializeBoard(50)
for move in moves:
    direction = move.split()[0]
    num_moves = int(move.split()[-1])
    for _ in range(num_moves):
        rope.move(direction)
        #print(f"Direction: {direction}")
        #printBoard(rope, board)
        ##input()

print(len(rope.knots[-2].tail_positions))
print(rope.knots[-2].tail_positions)