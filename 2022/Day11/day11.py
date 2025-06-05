####### SETUP 
with open("day11_input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

ROUNDS = 20
####### PART 1
class Monkey():
    def __init__(self, id, starting_items, operation, test_case):
        self.id = id
        self.items = starting_items
        self.worry = lambda a : eval(f"{operation.split(" = ")[1].replace('old', str(a))}") //3
        self.test = lambda a : test_case["true"] if (a/test_case["val"]).is_integer() == 1 else test_case["false"]
        self.inspection_count = 0

    def throwItems(self):
        throwables = {}
        self.inspection_count += len(self.items)
        for item in self.items:
            new_item = self.worry(item)

            try:
                throwables[self.test(new_item)].append(new_item)
            except:
                throwables[self.test(new_item)] = [new_item]

        self.items = []

        return throwables

    def receiveItem(self, item):
        self.items.extend(item)

monkeys = {}
for group_index in range(0, len(lines), 7):
    monkey_id = int(lines[group_index].split()[1][:-1])
    starting_items = [int(item) for item in lines[group_index+1].split(": ")[1].split(", ")]
    operation = lines[group_index+2]
    test = {"val": int(lines[group_index+3].split()[-1]), "true": int(lines[group_index+4].split()[-1]), "false": int(lines[group_index+5].split()[-1])}

    monkeys[monkey_id] = Monkey(monkey_id, starting_items, operation, test)

for _ in range(ROUNDS):
    for id in range(len(monkeys)):
        throwables = monkeys[id].throwItems()
        if throwables:
            for receiving_monkey in throwables:
                monkeys[receiving_monkey].receiveItem(throwables[receiving_monkey])

sorted_count = sorted([monkeys[id].inspection_count for id in range(len(monkeys))])
print(f"PART 1 MONKEY BUSINESS: {sorted_count[-1] * sorted_count[-2]}")

####### PART 2
