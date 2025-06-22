####### SETUP 
with open("day13_input.txt", "r") as file:
    lines = file.readlines()

####### PART 1

def createList(line):
    list_queue = []
    current_val = ""
    for char in line:
        if char == "[":
            current_list = []
            if list_queue:
                list_queue[-1].append(current_list)
            list_queue.append(current_list)
        elif char == "," and current_val:
            current_list.append(int(current_val))
            current_val = ""
        elif char == "]":
            if current_val:
                current_list.append(int(current_val))
                current_val = ""
            if len(list_queue) > 1:
                list_queue.pop()
                current_list = list_queue[-1]
            else:
                return list_queue[0]
        elif char != ",":
            current_val += char

def compareLists(pair):
    list1, list2 = pair[0], pair[1]

    

pair = []
pair_counter = 1
total = 0
for line in lines:
    if line:
        pairs.append(createList(line.strip()))
    else:
        if compareLists(pair):
            total += pair_counter

        pair.clear()
        pair_counter = 0