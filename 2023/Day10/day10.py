####### SETUP
with open("day10_input.txt", "r") as file:
    lines = file.readlines()
board = [list(line.strip()) for line in lines]
for y, line in enumerate(board):
    for x, char in enumerate(line):
        if char == "S":
            start_pos = [y, x]

####### PART 1
ORTHOGONAL = [[1,0], [-1,0], [0,1], [0,-1]]
DIRECTIONS = {"|": [[1,0], [-1,0]], 
              "-": [[0,1], [0,-1]], 
              "L": [[-1,0], [0,1]], 
              "J": [[-1,0], [0,-1]],
              "7": [[1,0], [0,-1]],
              "F": [[1,0], [0,1]],
              ".": []
              }

nodes = [start_pos]
for direction in ORTHOGONAL:
    pos = [start_pos[0] + direction[0], start_pos[1] + direction[1]]

    for pipe_direction in DIRECTIONS[board[pos[0]][pos[1]]]:
        validate_pos = [pos[0] + pipe_direction[0], pos[1] + pipe_direction[1]]
        if validate_pos == start_pos:
            nodes.append(pos)

current_node = nodes[1]
while True:
    pipe = board[current_node[0]][current_node[1]]
    node_a = [current_node[0] + DIRECTIONS[pipe][0][0], current_node[1] + DIRECTIONS[pipe][0][1]]
    node_b = [current_node[0] + DIRECTIONS[pipe][1][0], current_node[1] + DIRECTIONS[pipe][1][1]]

    if node_a in nodes and node_b in nodes:
        break
    elif node_a in nodes:
        nodes.append(node_b)
        current_node = node_b
    else:
        nodes.append(node_a)
        current_node = node_a

print(f"PART 1 FARTHEST NODE: {len(nodes)//2}")