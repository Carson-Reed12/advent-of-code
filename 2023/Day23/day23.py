import networkx as nx
####### SETUP
with open("day23_input.txt", "r") as file:
    lines = file.readlines()
board = [line.strip() for line in lines]

SIZE = len(board)
####### PART 1
# G = nx.DiGraph()

# for y, line in enumerate(board):
#     for x, char in enumerate(line):
#         if char != "#":
#             G.add_node(str([y,x]))
#             if y == 0:
#                 start_node = str([y,x])
#             elif y == SIZE-1:
#                 end_node = str([y,x])

# omni_directions = [[0,1], [0,-1], [1,0], [-1,0]]
# arrow_directions = {">": [0,1], "v": [1,0], "<": [0,-1], "^": [-1,0]}
# for node in G.nodes:
#     node_coord = [int(node.split(",")[0][1:]), int(node.split(",")[1][:-1])]
#     char = board[node_coord[0]][node_coord[1]]

#     if char == ".":
#         for direction in omni_directions:
#             next_coord = [node_coord[0] + direction[0], node_coord[1] + direction[1]]
#             if 0 <= next_coord[0] < SIZE and 0 <= next_coord[1] < SIZE:
#                 if board[next_coord[0]][next_coord[1]] != "#":
#                     G.add_edge(node, str(next_coord))
#     elif char != "#":
#         next_coord = [node_coord[0] + arrow_directions[char][0], node_coord[1] + arrow_directions[char][1]]
#         if 0 <= next_coord[0] < SIZE and 0 <= next_coord[1] < SIZE:
#             if board[next_coord[0]][next_coord[1]] != "#":
#                 G.add_edge(node, str(next_coord))

# longest_hike = 0
# longest_paths = nx.all_simple_paths(G, start_node, end_node)
# for path in longest_paths:
#     if len(path) > longest_hike:
#         longest_hike = len(path)
# print(f"PART 1 LONGEST HIKE: {longest_hike-1}")

####### PART 2
G = nx.DiGraph()

for y, line in enumerate(board):
    for x, char in enumerate(line):
        if char != "#":
            G.add_node(str([y,x]))
            if y == 0:
                start_node = str([y,x])
            elif y == SIZE-1:
                end_node = str([y,x])

omni_directions = [[0,1], [0,-1], [1,0], [-1,0]]
for node in G.nodes:
    node_coord = [int(node.split(",")[0][1:]), int(node.split(",")[1][:-1])]
    char = board[node_coord[0]][node_coord[1]]

    if char != "#":
        for direction in omni_directions:
            next_coord = [node_coord[0] + direction[0], node_coord[1] + direction[1]]
            if 0 <= next_coord[0] < SIZE and 0 <= next_coord[1] < SIZE:
                if board[next_coord[0]][next_coord[1]] != "#":
                    G.add_edge(node, str(next_coord))

longest_hike = 0 # 5883
longest_paths = nx.all_simple_paths(G, start_node, end_node) # [2350:] 
for i, path in enumerate(longest_paths):
    print(f"\r{i} - {longest_hike}", end="", flush=True)
    if len(path) > longest_hike:
        longest_hike = len(path)
print(f"\nPART 2 LONGEST HIKE: {longest_hike-1}")