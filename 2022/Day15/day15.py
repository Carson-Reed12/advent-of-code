import re
####### SETUP
with open("day15_input.txt", "r") as file:
    line_sensors = file.readlines()
line_sensors = [line_sensor.strip() for line_sensor in line_sensors]

####### PART 1 
class Sensor():
    def __init__(self, line):
        positions = re.findall(r'x=-?\d+, y=-?\d+', line)
        sensor_coords = positions[0]
        beacon_coords = positions[1]

        self.pos = [int(sensor_coords.split(", ")[0].split("=")[1]), int(sensor_coords.split(", ")[1].split("=")[1])]
        self.closest_beacon = [int(beacon_coords.split(", ")[0].split("=")[1]), int(beacon_coords.split(", ")[1].split("=")[1])]
        self.distance = abs(self.pos[0] - self.closest_beacon[0]) + abs(self.pos[1] - self.closest_beacon[1]) 

    def lineLength(self, y_val):
        # Relies on the fact that the sensor range makes a diamond
        # For every y value away from the sensor pos, the length is one shorter on either end
        y_offset = abs(y_val - self.pos[1])
        if y_offset > self.distance:
            return []

        total_positions = [self.pos[0] - self.distance + y_offset, self.pos[0] + self.distance - y_offset]
        return total_positions


def mergeRanges(arr1, arr2):
    if arr2[1]+1 < arr1[0]:
        return arr1, arr2
    if arr2[0]-1 > arr1[1]:
        return arr1, arr2
    return [min([arr1[0], arr2[0]]), max([arr1[1], arr2[1]])], None

def mergeAll(master_ranges):
    while True:
        merged_range = None
        pop_indices = []
        for i in range(len(master_ranges)):
            for j in range(i+1, len(master_ranges)):
                merge1, merge2 = mergeRanges(master_ranges[i], master_ranges[j])
                if not merge2:
                    merged_range = merge1
                    super_break = True
                    pop_indices = [j, i]
                    break
            if super_break:
                break

        for index in pop_indices:
            master_ranges.pop(index)

        if merged_range:
            master_ranges.append(merged_range)
        else:
            break

    return master_ranges
        
sensors = [Sensor(line) for line in line_sensors] 
master_ranges = []
for sensor in sensors:
    sensor_range = sensor.lineLength(2000000)
    if sensor_range:
        master_ranges.append(sensor_range)

master_ranges = mergeAll(master_ranges)
print(f"PART 1 NON-BEACON LOCATIONS: {master_ranges[0][1] - master_ranges[0][0]}")

####### PART 2
for y in range(4000001):
    print(f"\rSearching line {y}", end="", flush=True)
    master_ranges = []
    for sensor in sensors:
        sensor_range = sensor.lineLength(y)
        if sensor_range:
            master_ranges.append(sensor_range)

    master_ranges = mergeAll(master_ranges)
    if len(master_ranges) > 1:
        x = min(master_ranges[0][1], master_ranges[1][1])+1
        print(f"\nBeacon found! Location: x={x}, y={y}")
        print(f"PART 2 BEACON FREQUENCY: {(x*4000000)+y}")
        break
