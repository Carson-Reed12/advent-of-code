####### SETUP
with open("day4_input.txt", "r") as file:
    lines = file.readlines()
cards = [line.strip() for line in lines]

####### PART 1
total_points = 0
for card in cards:
    sets = card.split(": ")[1].split(" | ")
    matches = set(sets[0].split()).intersection(set(sets[1].split()))

    total_points += 2 ** (len(matches) - 1) if len(matches) > 0 else 0
print(f"PART 1 TOTAL POINTS: {total_points}")

####### PART 2
card_count = {id+1: 0 for id in range(len(cards))}

for card in cards:
    id = int(card.split(":")[0].split()[1])
    card_count[id] += 1

    sets = card.split(": ")[1].split(" | ")
    matches = set(sets[0].split()).intersection(set(sets[1].split()))

    for i in range(len(matches)):
        card_count[id + i + 1] += card_count[id]

print(f"PART 2 TOTAL POINTS: {sum(card_count.values())}")