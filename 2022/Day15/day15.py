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
        # Relies on the fact that the sensor makes a diamond
        # For every y value away from the sensor pos, the length is one shorter on either end
        # If this idea doesn't work, will have to figure out numerically. Wouldn't be hard except for determining overlap
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
        

#### PART 2
sensors = [Sensor(line) for line in line_sensors] 
for i in range(4000001):
    print(f"\r{i}", end="", flush=True)
    master_ranges = []
    for sensor in sensors:
        sensor_range = sensor.lineLength(i)
        if sensor_range:
            master_ranges.append(sensor.lineLength(i))

    while True:
        new_merge = None
        poppers = []
        for j in range(len(master_ranges)):
            for k in range(j+1, len(master_ranges)):
                merge1, merge2 = mergeRanges(master_ranges[j], master_ranges[k])
                if not merge2:
                    new_merge = merge1
                    super_break = True
                    poppers = [k, j]
                    break
            if super_break:
                break
        for popper in poppers:
            master_ranges.pop(popper)
        if new_merge:
            master_ranges.append(new_merge)
        else:
            break

    if len(master_ranges) > 1:
        x = min(master_ranges[0][1], master_ranges[1][1])+1
        print()
        print(f"{x}, {i}")
        print((x*4000000)+i)
        
        
        input()


# for i in range(4000001):
#     master_positions = []
#     for sensor in sensors:
#         master_positions.extend(sensor.lineLength(i))
#         if sensor.pos[1] == i:
#             master_positions.append(sensor.pos[0])
#         if sensor.closest_beacon[1] == i:
#             master_positions.append(sensor.closest_beacon[0])
# 
#     master_positions = list(set(master_positions))
#     if master_positions[0] == 0 and master_positions[4000000] == 4000000:
#         print(f"{i}: FULL")
#     else:
#         print(f"{i}: NOT FULL")
#         for j in range(4000001):
#             if j not in master_positions:
#                 print(f"FINAL BEACON: {j}, {i}")
#                 print(f"FREQUENCY: {(j*4000000)+i}")
#                 break
# 
