import re
####### SETUP
with open("day2_input.txt", "r") as file:
    lines = file.readlines()

game_counter = 1
games = {}
for game in [line.strip() for line in lines]:
    pulls = game.split(": ")[1].split(";")
    games[game_counter] = pulls
    game_counter += 1

LIMITS = {"red": 12, "green": 13, "blue": 14}
####### PART 1
total = 0
for id in games.keys():
    valid = True
    pulls = games[id]
    for pull in pulls:
        for color in pull.split(","):
            if "red" in color:
                if int(re.search("\d+", color).group()) > LIMITS["red"]:
                    valid = False
            elif "green" in color:
                if int(re.search("\d+", color).group()) > LIMITS["green"]:
                    valid = False
            elif "blue" in color:
                if int(re.search("\d+", color).group()) > LIMITS["blue"]:
                    valid = False

    if valid:
        total += id

print(f"PART 1 VALID ID SUM: {total}")

####### PART 2
total = 0
for id in games.keys():
    min_colors = {"red": 0, "green": 0, "blue": 0}
    pulls = games[id]
    for pull in pulls:
        for color in pull.split(","):
            if "red" in color:
                val = int(re.search("\d+", color).group())
                if val > min_colors["red"]:
                    min_colors["red"] = val
            elif "green" in color:
                val = int(re.search("\d+", color).group())
                if val > min_colors["green"]:
                    min_colors["green"] = val
            elif "blue" in color:
                val = int(re.search("\d+", color).group())
                if val > min_colors["blue"]:
                    min_colors["blue"] = val

    total += min_colors["red"] * min_colors["green"] * min_colors["blue"]
print(f"PART 2 VALID ID SUM: {total}")