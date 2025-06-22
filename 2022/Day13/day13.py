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

    for val1, val2 in zip(list1, list2):
        if isinstance(val1, int) and isinstance(val2, int):
            if val1 < val2: return True
            elif val1 > val2: return False
        elif isinstance(val1, list) and isinstance(val2, list):
            comparison = compareLists([val1, val2])
            if comparison != -1:
                return comparison
        else:
            if isinstance(val1, int):
                listed_val1 = [val1]
                comparison = compareLists([listed_val1, val2])
                if comparison != -1:
                    return comparison
            else:
                listed_val2 = [val2]
                comparison = compareLists([val1, listed_val2])
                if comparison != -1:
                    return comparison

    if len(list1) < len(list2):
        return True
    elif len(list1) > len(list2):
        return False
    else:
        return -1

pair = []
pair_counter = 1
total = 0
for line in lines:
    if line != "\n":
        pair.append(createList(line.strip()))
    if len(pair) == 2:
        if compareLists(pair):
            total += pair_counter

        pair.clear()
        pair_counter += 1

print(f"PART 1 PAIR SUM: {total}")

####### PART 2
def sortLists(all_lists):
    for i in range(len(all_lists)):
        swapped = False
        for j in range(len(all_lists) - i - 1):
            if not compareLists([all_lists[j], all_lists[j+1]]):
                all_lists[j], all_lists[j+1] = all_lists[j+1], all_lists[j]
                swapped = True
        # if not swapped:
        #     break


all_lists = [createList(line.strip()) for line in lines if line != "\n"]
all_lists.extend([[2], [6]])
sortLists(all_lists)
decoder_key = (all_lists.index([2]) + 1) * (all_lists.index([6]) + 1)
print(f"PART 2 DECODER KEY: {decoder_key}")