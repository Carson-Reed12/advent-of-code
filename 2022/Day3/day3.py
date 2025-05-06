import string
####### SETUP
with open("day3_input.txt", "r") as file:
    rucksack_lines = [line.strip() for line in file.readlines()]

####### PART 1
ITEM_SCORE = {letter: i+1 for i, letter in enumerate(string.ascii_letters)}

class Rucksack():
    def __init__(self, rucksack):
        self.rucksack = rucksack
        self.left_rucksack = rucksack[:len(rucksack)//2]
        self.right_rucksack = rucksack[len(rucksack)//2:]

        self.left_map = self.getMap(self.left_rucksack)
        self.right_map = self.getMap(self.right_rucksack)

        self.error_item = self.getError(self.left_map, self.right_map)

    def getMap(self, rucksack):
        item_map = {letter: 0 for letter in string.ascii_letters}
        for item in rucksack:
            item_map[item] += 1
        return item_map
    
    def getError(self, left_map, right_map):
        for letter in string.ascii_letters:
            if left_map[letter] != 0 and right_map[letter] != 0:
                return letter

rucksacks = [Rucksack(rucksack_line) for rucksack_line in rucksack_lines]
total_priorities = 0
for rucksack in rucksacks:
    total_priorities += ITEM_SCORE[rucksack.error_item]
print(f"PART 1 TOTAL PRIORITIES: {total_priorities}")

####### PART 2
total_priorities = 0
for rucksack1, rucksack2, rucksack3 in list(zip(rucksacks[::3], rucksacks[1::3], rucksacks[2::3])):
    rucksack1_item_map = rucksack1.getMap(rucksack1.rucksack)
    rucksack2_item_map = rucksack1.getMap(rucksack2.rucksack)
    rucksack3_item_map = rucksack1.getMap(rucksack3.rucksack)

    for letter in string.ascii_letters:
        if rucksack1_item_map[letter] != 0 and rucksack2_item_map[letter] != 0 and rucksack3_item_map[letter] != 0:
            total_priorities += ITEM_SCORE[letter]
            break
print(f"PART 2 TOTAL PRIORITIES: {total_priorities}")