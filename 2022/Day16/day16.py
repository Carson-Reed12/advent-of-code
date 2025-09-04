import re

####### SETUP
with open("day16_input.txt", "r") as file:
    valve_lines = file.readlines()


####### PART 1
class Valve:
    def __init__(self, line):
        self.id = re.search(r"Valve (\w\w) has", line).group(1)
        self.rate = int(re.search(r"\d+", line).group())
        self.neighbors = re.search(r"valves? (.*)", line).group(1).split(", ")

    def print(self):
        print(f"{self.id} - Rate: {self.rate}, Neighbors: {self.neighbors}")


def maxPressure(valve, activated, depth, pressure, last_nodes):
    if depth == 0:
        return pressure

    scores = []
    if valve not in activated and valve.rate != 0:
        scores.append(
            maxPressure(
                valve,
                activated + [valve],
                depth - 1,
                pressure + valve.rate * (depth - 1),
                [],
            )
        )
    for neighbor in valve.neighbors:
        if neighbor not in last_nodes:
            scores.append(
                maxPressure(
                    valves[neighbor],
                    activated,
                    depth - 1,
                    pressure,
                    last_nodes + [valve.id],
                )
            )

    if not scores:
        return pressure
    if max(scores) > current_max:
        current_max = max(scores)
    return max(scores)


valves = {
    re.search(r"Valve (\w\w) has", line).group(1): Valve(line) for line in valve_lines
}
starting_valve = [valves[valve_id] for valve_id in valves if valve_id == "AA"][0]
starting_valve.print()
max_pressure = maxPressure(starting_valve, [], 30, 0, [])
print(f"PART 1 MAX PRESSURE: {max_pressure}")
