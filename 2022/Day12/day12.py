import networkx as nx
####### SETUP 
with open("day12_input.txt", "r") as file:
    heightmap = [list(line.strip()) for line in file.readlines()]

SIZE_Y = len(heightmap)
SIZE_X = len(heightmap[0])

####### PART 1
def validNode(source_node, dest_node):
    heights = "SabcdefghijklmnopqrstuvwxyzE"
    source_height = heightmap[source_node[0]][source_node[1]]
    dest_height = heightmap[dest_node[0]][dest_node[1]]

    if heights.index(dest_height) <= heights.index(source_height) + 1:
        return True
    else:
        return False

G = nx.DiGraph()

starting_nodes = []
for y, line in enumerate(heightmap):
    for x, char in enumerate(line):
        if char == "S" or char == "a":
            starting_nodes.append(str([y,x]))

        if char == "S":
            start_node = str([y,x])
        elif char == "E":
            end_node = str([y,x])
        G.add_node(str([y,x]))

directions = [[0,1], [0,-1], [1,0], [-1,0]]
for node in G.nodes():
    source_coord = [int(val) for val in node[1:-1].split(", ")]
    for direction in directions:
        dest_coord = [source_coord[0] + direction[0], source_coord[1] + direction[1]]
        if 0 <= dest_coord[0] < SIZE_Y and 0 <= dest_coord[1] < SIZE_X:
            if validNode(source_coord, dest_coord):
                G.add_edge(node, str(dest_coord))

shortest_path = nx.shortest_path_length(G, start_node, end_node)
print(f"PART 1 SHORTEST PATH: {shortest_path}")

####### PART 2
minimum_path = float('inf')
for starting_node in starting_nodes:
    try:
        shortest_path = nx.shortest_path_length(G, starting_node, end_node)
        if shortest_path < minimum_path:
            minimum_path = shortest_path
    except:
        pass       

print(f"PART 2 SHORTEST PATH: {minimum_path}")
