import networkx as nx
####### SETUP
with open("day17_input.txt", "r") as file:
    lines = file.readlines()

board = []
for line in lines:
    blocks = [int(block) for block in list(line.strip())]
    board.append(blocks)

SIZE = len(board)

####### PART 1
G = nx.DiGraph()
nodes = {}

start_node = (str([0,0]), "E", 3)
G.add_node(start_node)
for i, line in enumerate(board):
    for j, char in enumerate(line):
        for dir in "NESW":
            for level in range(3):
                G.add_node((str([i,j]), dir, level))

for dir in "NESW":
    for level in range(3):
        G.add_edge((str([SIZE-1,SIZE-1]), dir, level), "end", weight=0)

directions = {"N": [-1,0], "E": [0,1], "S": [1,0], "W": [0,-1]}
toggle_dir = lambda a : ("S" if a == "N" else "N") if a in ["N", "S"] else ("E" if a == "W" else "W")
for node, dir, level in G.nodes:
    if node not in "end":
        coord0 = int(node.split(",")[0][1:])
        coord1 = int(node.split(",")[1][:-1])

        remaining_dirs = list("NESW")
        remaining_dirs.remove(toggle_dir(dir))

        for remaining_dir in remaining_dirs:
            if (0 <= coord0 + directions[remaining_dir][0] < SIZE) and (0 <= coord1 + directions[remaining_dir][1] < SIZE):
                next_coord = [coord0 + directions[remaining_dir][0], coord1 + directions[remaining_dir][1]]
                block = board[coord0 + directions[remaining_dir][0]][coord1 + directions[remaining_dir][1]]

                if remaining_dir != dir:
                    G.add_edge((node, dir, level), (str(next_coord), remaining_dir, 2), weight=block)
                elif level != 0:
                    G.add_edge((node, dir, level), (str(next_coord), dir, level-1), weight=block)

lowest_score = nx.shortest_path_length(G, start_node, "end", weight="weight")
print(f"PART 1 LOWEST SCORE: {lowest_score}")

####### PART 2
G = nx.DiGraph()
nodes = {}

start_node = (str([0,0]), "E", 10)
G.add_node(start_node)
for i, line in enumerate(board):
    for j, char in enumerate(line):
        for dir in "NESW":
            for level in range(10):
                G.add_node((str([i,j]), dir, level))

for dir in "NESW":
    for level in range(7):
        G.add_edge((str([SIZE-1,SIZE-1]), dir, level), "end", weight=0)

directions = {"N": [-1,0], "E": [0,1], "S": [1,0], "W": [0,-1]}
toggle_dir = lambda a : ("S" if a == "N" else "N") if a in ["N", "S"] else ("E" if a == "W" else "W")
for node, dir, level in G.nodes:
    if node not in "end":
        coord0 = int(node.split(",")[0][1:])
        coord1 = int(node.split(",")[1][:-1])

        remaining_dirs = list("NESW")
        remaining_dirs.remove(toggle_dir(dir))

        if level >= 7:
            if (0 <= coord0 + directions[dir][0] < SIZE) and (0 <= coord1 + directions[dir][1] < SIZE):
                next_coord = [coord0 + directions[dir][0], coord1 + directions[dir][1]]
                block = board[coord0 + directions[dir][0]][coord1 + directions[dir][1]]
                G.add_edge((node, dir, level), (str(next_coord), dir, level-1), weight=block)
        else:
            for remaining_dir in remaining_dirs:
                if (0 <= coord0 + directions[remaining_dir][0] < SIZE) and (0 <= coord1 + directions[remaining_dir][1] < SIZE):
                    next_coord = [coord0 + directions[remaining_dir][0], coord1 + directions[remaining_dir][1]]
                    block = board[coord0 + directions[remaining_dir][0]][coord1 + directions[remaining_dir][1]]

                    if remaining_dir != dir:
                        G.add_edge((node, dir, level), (str(next_coord), remaining_dir, 9), weight=block)
                    elif level != 0:
                        G.add_edge((node, dir, level), (str(next_coord), dir, level-1), weight=block)

lowest_score = nx.shortest_path_length(G, start_node, "end", weight="weight")
print(f"PART 2 LOWEST SCORE: {lowest_score}")