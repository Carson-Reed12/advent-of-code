import networkx as nx
####### SETUP
with open("day21_input.txt", "r") as file:
    lines = file.readlines()

board = []
for line in lines:
    board.append(line.strip())

SIZE = len(board)
####### PART 1
G = nx.DiGraph()

for y, line in enumerate(board):
    for x, char in enumerate(line):
        if char == "." or char == "S":
            G.add_node(str([y,x]))
        if char == "S":
            start_node = str([y,x])

directions = [[0,1],[0,-1],[1,0],[-1,0]]
for node in G.nodes:
    y_val = int(node.split(",")[0][1:])
    x_val = int(node.split(",")[1][:-1])

    for direction in directions:
        if (0 <= y_val+direction[0] < SIZE) and (0 <= x_val+direction[1] < SIZE):
            if board[y_val+direction[0]][x_val+direction[1]] == ".":
                G.add_edge(node, str([y_val+direction[0], x_val+direction[1]]))

total = 0
for val in nx.shortest_path_length(G, start_node).values():
    if val <= 64 and val %2 == 0:
        total += 1
print(f"PART 1 TOTAL PLOTS: {total}")