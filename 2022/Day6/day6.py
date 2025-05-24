####### SETUP
with open("day6_input.txt", "r") as file:
    datastream = file.readlines()[0]

####### PART 1
def findMarker(datastream, length):
    stack = []
    for index, char in enumerate(datastream.strip()):
        if len(stack) != length:
            stack.append(char)
        else:
            if len(stack) == len(set(stack)):
                return index
            else:
                stack.append(char)
                stack.pop(0)
    return -1

print(f"PART 1 MARKER INDEX: {findMarker(datastream, 4)}")      

####### PART 2
print(f"PART 2 MESSAGE INDEX: {findMarker(datastream, 14)}")      