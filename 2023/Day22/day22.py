import copy
####### SETUP
with open("day22_input.txt", "r") as file:
    brick_coordinates = [line.strip() for line in file.readlines()]

####### PART 1
class Brick:
    def __init__(self, brick_coordinates):
        brick_start = [int(val) for val in brick_coordinates.split("~")[0].split(",")]
        brick_end = [int(val) for val in brick_coordinates.split("~")[1].split(",")]

        if brick_start[0] != brick_end[0]: self.points = [[i, brick_start[1], brick_start[2]] for i in range(brick_start[0], brick_end[0]+1)]
        if brick_start[1] != brick_end[1]: self.points = [[brick_start[0], i, brick_start[2]] for i in range(brick_start[1], brick_end[1]+1)]
        if brick_start[2] != brick_end[2]: self.points = [[brick_start[0], brick_start[1], i] for i in range(brick_start[2], brick_end[2]+1)]

        self.on_ground = self.checkOnGround()
        # def fall decreases all z by 1
        # def collision checks if any brick points are the same

    def checkOnGround(self):
        return any(point[2] == 1 for point in self.points)

    def fall(self):
        for point in self.points:
            point[2] -= 1 if point[2] > 1 else 0
        self.on_ground = self.checkOnGround()

    def checkCollision(self, brick):
        check_points = copy.deepcopy(self.points)
        for point in check_points:
            point[2] -= 1 if point[2] > 1 else 0
        
        for point in brick.points:
            if point in check_points:
                return True
        return False
    
def settleBricks(bricks):
    falling = True
    while falling:
        falling = False
        for brick in bricks:
            if not brick.on_ground:
                other_bricks = [other_brick for other_brick in bricks if other_brick != brick]
                if all(not brick.checkCollision(other_brick) for other_brick in other_bricks):
                    brick.fall()
                    falling = True
    return bricks

settled_bricks = settleBricks([Brick(line) for line in brick_coordinates])
for brick in settled_bricks:
    print(brick.points)
    print("---")
# now need to check for disintegrations