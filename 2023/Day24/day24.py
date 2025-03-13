####### SETUP
with open("day24_input.txt", "r") as file:
    hail_stats = [line.strip() for line in file.readlines()]

LOWER_BOUND = 200000000000000
UPPER_BOUND = 400000000000000
####### PART 1
class Hail():
    def __init__(self, stats, xy_only = False): # will need to update this for part 2 and change the input to 0 all the Z stuff for part 1
        initial_position = [int(val) for val in stats.split("@")[0][:-1].split(", ")] # px, py, pz
        velocities = [int(val) for val in stats.split("@")[1][1:].split(", ")] # vx, vy, vz

        if xy_only:
            initial_position[2] = 0
            velocities[2] = 0

        self.initial_position = initial_position
        self.velocities = velocities
        self.stats = stats
        self.slope_xy = velocities[1] / velocities[0]
        self.b_xy = initial_position[1] - (self.slope_xy * initial_position[0])

    def calculateY(self, x):
        return (self.slope_xy * x) + self.b_xy
    
    def pastCheck(self, x):
        if x >= self.initial_position[0] and self.velocities[0] > 0:
            return True
        elif x <= self.initial_position[0] and self.velocities[0] < 0:
            return True
        else:
            return False

    def intersects(self, hail):
        if self.slope_xy == hail.slope_xy:
            return False
        
        x = (hail.b_xy - self.b_xy) / (self.slope_xy - hail.slope_xy)
        y = self.calculateY(x)

        if LOWER_BOUND <= x <= UPPER_BOUND and LOWER_BOUND <= y <= UPPER_BOUND and self.pastCheck(x) and hail.pastCheck(x):
            return True
        else:
            return False
    
hail = [Hail(stat, True) for stat in hail_stats]
checked_hail = []
total = 0
for hail1 in hail:
    checked_hail.append(hail1)
    for hail2 in hail:
        if hail2 not in checked_hail:
            if hail1.intersects(hail2):
                total += 1

print(total)

####### PART 2