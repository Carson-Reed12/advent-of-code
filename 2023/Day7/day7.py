import copy
####### SETUP
with open("day7_input.txt", "r") as file:
    lines = file.readlines()
hands = {}
for line in lines:
    hands[line.strip().split()[0]] = {"bid": int(line.strip().split()[1])}

####### PART 1
CARD_TYPES = "23456789TJQKA"

def handType(hand):
    card_counts = {card: 0 for card in CARD_TYPES}
    for card in hand:
        card_counts[card] += 1
    
    counts = card_counts.values()
    if 5 in counts:
        return "5k"
    elif 4 in counts:
        return "4k"
    elif 2 in counts and 3 in counts:
        return "fh"
    elif 3 in counts:
        return "3k"
    elif 2 in counts:
        if len([count for count in counts if count == 2]) == 2:
            return "2p"
        else:
            return "1p"
    else:
        return "hc"

for hand in hands:
    hands[hand]["type"] = handType(hand)

rank = 1
for hand_type in ["hc", "1p", "2p", "3k", "fh", "4k", "5k"]:
    sorted_hands = sorted([hand for hand in hands if hands[hand]["type"] == hand_type], key = lambda hand : [CARD_TYPES.index(card) for card in hand])
    for hand in sorted_hands:
        hands[hand]["rank"] = rank
        rank +=1

total_winnings = 0
for hand in hands:
    total_winnings += hands[hand]["rank"] * hands[hand]["bid"]
print(f"PART 1 TOTAL WINNINGS: {total_winnings}")

####### PART 2
CARD_TYPES_WILD = "J23456789TQKA"

def handTypeWild(hand):
    card_counts = {card: 0 for card in CARD_TYPES_WILD}
    for card in hand:
        card_counts[card] += 1

    hand_types = ["5k", "4k", "fh", "3k", "2p", "1p", "hc"]
    hand_type = 6
    for card in CARD_TYPES_WILD[1:]:
        new_counts = copy.deepcopy(card_counts)
        new_counts[card] += new_counts["J"]
        new_counts["J"] = 0
        counts = new_counts.values()

        if 5 in counts:
            hand_type = 0
        elif 4 in counts:
            if hand_type > hand_types.index("4k"):
                hand_type = hand_types.index("4k")
        elif 2 in counts and 3 in counts:
            if hand_type > hand_types.index("fh"):
                hand_type = hand_types.index("fh")
        elif 3 in counts:
            if hand_type > hand_types.index("3k"):
                hand_type = hand_types.index("3k")
        elif 2 in counts:
            if len([count for count in counts if count == 2]) == 2:
                if hand_type > hand_types.index("2p"):
                    hand_type = hand_types.index("2p")
            else:
                if hand_type > hand_types.index("1p"):
                    hand_type = hand_types.index("1p")
    return hand_types[hand_type]

for hand in hands:
    hands[hand]["type"] = handTypeWild(hand)

rank = 1
for hand_type in ["hc", "1p", "2p", "3k", "fh", "4k", "5k"]:
    sorted_hands = sorted([hand for hand in hands if hands[hand]["type"] == hand_type], key = lambda hand : [CARD_TYPES_WILD.index(card) for card in hand])
    for hand in sorted_hands:
        hands[hand]["rank"] = rank
        rank += 1

total_winnings = 0
for hand in hands:
    total_winnings += hands[hand]["rank"] * hands[hand]["bid"]
print(f"PART 2 TOTAL WINNINGS: {total_winnings}")