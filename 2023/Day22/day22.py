import copy
####### SETUP
with open("day22_input.txt", "r") as file:
    brick_coordinates = [line.strip() for line in file.readlines()]

####### PART 1
class Brick:
    def __init__(self, id, brick_coordinates):
        self.id = id
        brick_start = [int(val) for val in brick_coordinates.split("~")[0].split(",")]
        brick_end = [int(val) for val in brick_coordinates.split("~")[1].split(",")]

        if brick_start[0] != brick_end[0]: self.points = [[i, brick_start[1], brick_start[2]] for i in range(brick_start[0], brick_end[0]+1)] # will probably have to convert to ranges cause taking a long time
        elif brick_start[1] != brick_end[1]: self.points = [[brick_start[0], i, brick_start[2]] for i in range(brick_start[1], brick_end[1]+1)]
        elif brick_start[2] != brick_end[2]: self.points = [[brick_start[0], brick_start[1], i] for i in range(brick_start[2], brick_end[2]+1)]
        else: self.points = [[brick_start[0], brick_start[1], brick_start[2]]]

        self.on_ground = self.checkOnGround()

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

def disintegratableBricks(bricks):
    supported_by = {brick.id: [] for brick in bricks}
    disintegratable_bricks = [brick.id for brick in bricks]
    for brick1 in bricks:
        for brick2 in bricks:
            if brick1 != brick2 and brick1.checkCollision(brick2):
                supported_by[brick1.id].append(brick2.id)
    
    for brick in supported_by:
        if len(supported_by[brick]) == 1:
            if supported_by[brick][0] in disintegratable_bricks:
                disintegratable_bricks.remove(supported_by[brick][0])
    return disintegratable_bricks, supported_by

print("Settling bricks...")
settled_bricks = settleBricks([Brick(i, line) for i, line in enumerate(brick_coordinates)])
print("Checking disintegrations...")
disintegratable_bricks, supported_by = disintegratableBricks(settled_bricks)
print(f"PART 1 TOTAL DISINTEGRATIONS: {len(disintegratable_bricks)}")

####### PART 2
def convertSupports(supported_by):
    bricks_supported = {id: [] for id in supported_by}

    for id in supported_by:
        for brick in supported_by[id]:
            bricks_supported[brick].append(id)

    return bricks_supported

def fallingCount(initial_id, supported_by, bricks_supported):
    supports = copy.deepcopy(supported_by)
    queue = [initial_id]
    total = 0

    while queue:
        brick = queue.pop()
        for supported_brick in bricks_supported[brick]:
            supports[supported_brick].remove(brick)
            if not supports[supported_brick]:
                queue.append(supported_brick)
                total += 1
    
    return total

bricks_supported = convertSupports(supported_by)
falling_count = 0
for i in supported_by:
    falling_count += fallingCount(i, supported_by, bricks_supported)
print(f"PART 2 TOTAL FALLING: {falling_count}")