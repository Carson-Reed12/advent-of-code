from itertools import combinations
####### SETUP
with open("day11_input.txt", "r") as file:
    lines = file.readlines()
board = []
for line in lines:
    board.append(list(line.strip()))

####### PART 1
galaxies = []
for y, line in enumerate(board):
    for x, char in enumerate(line):
        if char == "#":
            galaxies.append([y,x])    

expand_rows = []
for y, line in enumerate(board):
    if all(char == "." for char in line):
        expand_rows.append(y)
expand_cols = []
for x in range(len(board[0])):
    galaxy_check = False
    for line in board:
        if line[x] == "#":
            galaxy_check = True
            break
    if not galaxy_check:
        expand_cols.append(x)

for galaxy in galaxies:
    orig_row = galaxy[0]
    orig_col = galaxy[1]
    for row in expand_rows:
        if orig_row > row:
            galaxy[0] += 1
    for col in expand_cols:
        if orig_col > col:
            galaxy[1] += 1

man_distance = lambda a, b : abs(a[0] - b[0]) + abs(a[1] - b[1])
total_lengths = 0
for pair in combinations(range(len(galaxies)), 2):
    total_lengths += man_distance(galaxies[pair[0]], galaxies[pair[1]])
print(f"PART 1 TOTAL LENGTHS: {total_lengths}")

####### PART 2
galaxies = []
for y, line in enumerate(board):
    for x, char in enumerate(line):
        if char == "#":
            galaxies.append([y,x])   

for galaxy in galaxies:
    orig_row = galaxy[0]
    orig_col = galaxy[1]
    for row in expand_rows:
        if orig_row > row:
            galaxy[0] += 999999
    for col in expand_cols:
        if orig_col > col:
            galaxy[1] += 999999

total_lengths = 0
for pair in combinations(range(len(galaxies)), 2):
    total_lengths += man_distance(galaxies[pair[0]], galaxies[pair[1]])
print(f"PART 2 TOTAL LENGTHS: {total_lengths}")