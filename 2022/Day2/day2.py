####### SETUP
with open("day2_input.txt", "r") as file:
    guide = file.readlines()

####### PART 1
OPPONENT_CHOICES = "ABC"
PLAYER_CHOICES = "XYZ"
SHAPE_SCORE = {"X": 1, "Y": 2, "Z": 3}

def resolveGame(opponent, player):
    rel_opponent = OPPONENT_CHOICES.index(opponent)
    rel_player = PLAYER_CHOICES.index(player)

    if rel_opponent == rel_player:
        return 3 + SHAPE_SCORE[player]
    elif rel_opponent == (rel_player - 1) % 3:
        return 6 + SHAPE_SCORE[player]
    else:
        return 0 + SHAPE_SCORE[player]

total = 0
for game in guide:
    opponent = game[0]
    player = game[2]

    total += resolveGame(opponent, player)
print(f"PART 1 TOTAL SCORE: {total}")

####### PART 2
def completeGame(opponent, result):
    rel_opponent = OPPONENT_CHOICES.index(opponent)

    if result == "Y":
        return 3 + SHAPE_SCORE[PLAYER_CHOICES[rel_opponent]]
    elif result == "Z":
        return 6 + SHAPE_SCORE[PLAYER_CHOICES[(rel_opponent + 1) % 3]]
    else:
        return 0 + SHAPE_SCORE[PLAYER_CHOICES[(rel_opponent - 1) % 3]]
    
total = 0
for game in guide:
    opponent = game[0]
    player = game[2]

    total += completeGame(opponent, player)
print(f"PART 2 TOTAL SCORE: {total}")