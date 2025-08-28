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

        total_positions = [[x, y_val] for x in range(self.pos[0] - self.distance + y_offset, self.pos[0] + self.distance - y_offset + 1)]
        # Location of closest beacon doesn't count
        if self.closest_beacon in total_positions:
            total_positions.remove(self.closest_beacon)
        return total_positions
        

# Could have some sort of function that returns a list of exclusive positions given a line number
# Then, extend all lists into one master list. Then make it a set, and get the length for the total count?
sensors = [Sensor(line) for line in line_sensors]
print(sensors[6].lineLength(10))

