####### SETUP
with open("day6_input.txt", "r") as file:
    lines = file.readlines()
times = [int(time) for time in lines[0].split() if time.isdigit()]
distances = [int(distance) for distance in lines[1].split() if distance.isdigit()]
races = [{"time": time, "distance": distance} for time, distance in zip(times, distances)]

####### PART 1
def winningRaces(race, show):
    wins = 0
    for i in range(race["time"]):
        if show: print(f"\r{i}", end="", flush=True)
        if i * (race["time"] - i) > race["distance"]:
            wins += 1
    return wins

total_wins = 1
for race in races:
    total_wins *= winningRaces(race, False)
print(f"PART 1 TOTAL WINS MULTIPLIED: {total_wins}")

####### PART 2
race = {"time": int(''.join([str(time) for time in times])), "distance": int(''.join([str(distance) for distance in distances]))}
total_wins = winningRaces(race, True)
print(f"\nPART 2 TOTAL WINS: {total_wins}")