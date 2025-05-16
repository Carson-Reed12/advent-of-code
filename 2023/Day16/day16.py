import copy
####### SETUP
with open("day16_input.txt", "r") as file:
    lines = file.readlines()
board = [list(line.strip()) for line in lines]
original_board = copy.deepcopy(board)
# display_board = copy.deepcopy(board)
SIZE = len(board)

def printBoard(board):
    for line in board:
        print(''.join(line))
        
####### PART 1
class Ray:
    def __init__(self, head, direction, start=False):
        self.head = head
        self.direction = direction
        self.complete = False

        if start:
            if board[self.head[0]][self.head[1]] == "\\":
                if self.direction == "RIGHT": self.direction = "DOWN"
                elif self.direction == "LEFT": self.direction = "UP"
                elif self.direction == "UP": self.direction = "LEFT"
                elif self.direction == "DOWN": self.direction = "RIGHT"
            elif board[self.head[0]][self.head[1]] == "/":
                if self.direction == "RIGHT": self.direction = "UP"
                elif self.direction == "LEFT": self.direction = "DOWN"
                elif self.direction == "UP": self.direction = "RIGHT"
                elif self.direction == "DOWN": self.direction = "LEFT"
            elif board[self.head[0]][self.head[1]] == "|":
                self.complete = True
            elif board[self.head[0]][self.head[1]] == "-":
                self.complete = True
            self.path = [head]
        else:
            self.path = []
    
    def move(self):
        directions = {"RIGHT": [0,1], "LEFT": [0,-1], "UP": [-1,0], "DOWN": [1,0]}
        self.head = [self.head[0] + directions[self.direction][0], self.head[1] + directions[self.direction][1]]

        if (self.head[0] < 0 or self.head[0] >= SIZE) or (self.head[1] < 0 or self.head[1] >= SIZE) or board[self.head[0]][self.head[1]] == "@":
            self.complete = True
        elif self.direction in ["RIGHT", "LEFT"] and board[self.head[0]][self.head[1]] == "|":
            self.complete = True
            board[self.head[0]][self.head[1]] = "@"
            # display_board[self.head[0]][self.head[1]] = "@"
            self.path.append(self.head)
            return [Ray(self.head, "UP"), Ray(self.head, "DOWN")]
        elif self.direction in ["UP", "DOWN"] and board[self.head[0]][self.head[1]] == "-":
            self.complete = True
            self.path.append(self.head)
            board[self.head[0]][self.head[1]] = "@"
            # display_board[self.head[0]][self.head[1]] = "@"
            return [Ray(self.head, "LEFT"), Ray(self.head, "RIGHT")]
        elif board[self.head[0]][self.head[1]] == "\\":
            if self.direction == "RIGHT": self.direction = "DOWN"
            elif self.direction == "LEFT": self.direction = "UP"
            elif self.direction == "UP": self.direction = "LEFT"
            elif self.direction == "DOWN": self.direction = "RIGHT"
            # display_board[self.head[0]][self.head[1]] = "#"
            self.path.append(self.head)
        elif board[self.head[0]][self.head[1]] == "/":
            if self.direction == "RIGHT": self.direction = "UP"
            elif self.direction == "LEFT": self.direction = "DOWN"
            elif self.direction == "UP": self.direction = "RIGHT"
            elif self.direction == "DOWN": self.direction = "LEFT"
            # display_board[self.head[0]][self.head[1]] = "#"
            self.path.append(self.head)
        else:
            # display_board[self.head[0]][self.head[1]] = "#"
            self.path.append(self.head)
        return []
    
def simulateRays(head, direction):
    start_ray = Ray(head, direction, start=True)
    if start_ray.complete and board[start_ray.head[0]][start_ray.head[1]] == "|" and direction in ["RIGHT", "LEFT"]:
        rays = [start_ray, Ray(start_ray.head, "UP"), Ray(start_ray.head, "DOWN")]
    elif start_ray.complete and board[start_ray.head[0]][start_ray.head[1]] == "-" and direction in ["UP", "DOWN"]:
        rays = [start_ray, Ray(start_ray.head, "LEFT"), Ray(start_ray.head, "RIGHT")]
    else:
        rays = [start_ray]

    while not all(ray.complete for ray in rays):
        new_rays = []
        for ray in rays:
            if not ray.complete:
                duplicated_rays = ray.move()
                new_rays.extend(duplicated_rays)
        rays.extend(new_rays)
    return rays

def countEnergy(rays):
    tiles = []
    for ray in rays:
        for tile in ray.path:
            if tile not in tiles:
                tiles.append(tile)
    return len(tiles)

print(f"PART 1 ENERGIZED TILES: {countEnergy(simulateRays([0,0], 'RIGHT'))}")

####### PART 2
max_energy = -1

for direction in ["RIGHT", "LEFT", "UP", "DOWN"]:
    for i in range(SIZE):
        board = copy.deepcopy(original_board)
        # display_board = copy.deepcopy(original_board)

        if direction == "RIGHT": start_head = [i, 0]
        if direction == "LEFT": start_head = [i, SIZE-1]
        if direction == "DOWN": start_head = [0, i]
        if direction == "UP": start_head = [SIZE-1, i]

        print(f"\r{start_head} - {direction    }", end="", flush=True)
        energy = countEnergy(simulateRays(start_head, direction))
        if energy > max_energy:
            max_energy = energy

print(f"\nPART 2 MAX ENERGY: {max_energy}")
