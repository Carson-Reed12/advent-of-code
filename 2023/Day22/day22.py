####### SETUP
with open("day22_input.txt", "r") as file:
    brick_coordinates = [line.strip() for line in file.readlines()]

####### PART 1
class Brick:
    def __init__(self, brick_coordinates):
        brick_start = brick_coordinates.split("~")[0]
        brick_end = brick_coordinates.split("~")[1]

        self.points = [] # may have to change to ranges for efficiency?
        # put in all points occupied
        # def fall decreases all z by 1
        # def collision checks if any brick points are the same
    