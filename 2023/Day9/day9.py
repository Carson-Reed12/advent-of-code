import copy
####### SETUP
with open("day9_input.txt", "r") as file:
    lines = file.readlines()
sequences = [[int(val) for val in line.strip().split()] for line in lines]

####### PART 1
extrapolated_sum = 0
for sequence in sequences:
    created_sequences = [sequence]
    next_sequence = sequence

    while not all(val == 0 for val in next_sequence):
        next_row = [next_sequence[i+1] - next_sequence[i] for i in range(len(next_sequence) - 1)]
        created_sequences.append(next_row)
        next_sequence = copy.deepcopy(next_row)

    lower_val = 0
    for sequence in reversed(created_sequences):
        lower_val += sequence[-1]
    extrapolated_sum += lower_val

print(f"PART 1 EXTRAPOLATED SUM: {extrapolated_sum}")

####### PART 2
extrapolated_sum = 0
for sequence in sequences:
    created_sequences = [sequence]
    next_sequence = sequence

    while not all(val == 0 for val in next_sequence):
        next_row = [next_sequence[i+1] - next_sequence[i] for i in range(len(next_sequence) - 1)]
        created_sequences.append(next_row)
        next_sequence = copy.deepcopy(next_row)

    lower_val = 0
    for sequence in reversed(created_sequences):
        lower_val = sequence[0] - lower_val
    extrapolated_sum += lower_val

print(f"PART 2 EXTRAPOLATED SUM: {extrapolated_sum}")