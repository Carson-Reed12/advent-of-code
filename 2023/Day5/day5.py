####### SETUP
with open("day5_input.txt", "r") as file:
    lines = file.readlines()

seeds = [int(value) for value in lines[0].split(": ")[1].split()]

MODES = ["s2s", "s2f", "f2w", "w2l", "l2t", "t2h", "h2l"]
conversion_map = {mode: [] for mode in MODES}

conversion_type = ""
for line in lines:
    if "seed-to-soil" in line:
        conversion_type = "s2s"
    elif "soil-to-fertilizer" in line:
        conversion_type = "s2f"
    elif "fertilizer-to-water" in line:
        conversion_type = "f2w"
    elif "water-to-light" in line:
        conversion_type = "w2l"
    elif "light-to-temperature" in line:
        conversion_type = "l2t"
    elif "temperature-to-humidity" in line:
        conversion_type = "t2h"
    elif "humidity-to-location" in line:
        conversion_type = "h2l"
    elif conversion_type != "" and line != "\n":
        conversion = [int(value) for value in line.strip().split()]
        conversion_map[conversion_type].append({"destination": conversion[0], "source": conversion[1], "range": conversion[2]})
        
####### PART 1
def convertType(source, type):
    for conversion in conversion_map[type]:
        if source in range(conversion["source"], conversion["source"] + conversion["range"]):
            return conversion["destination"] + (source - conversion["source"])
    return source

lowest_location = float("inf")
for seed in seeds:
    current_val = seed
    for mode in MODES:
        current_val = convertType(current_val, mode)
    if current_val < lowest_location:
        lowest_location = current_val
print(f"PART 1 LOWEST LOCATION: {lowest_location}")

####### PART 2 (need to optimize)
lowest_location = float("inf")
for i in range(0, len(seeds), 2):
    print(f"\n{seeds[i]} - {seeds[i] + seeds[i+1]}")
    for seed in range(seeds[i], seeds[i] + seeds[i+1]):
        print(f"\r{seed}", end="", flush=True)
        current_val = seed
        for mode in MODES:
            current_val = convertType(current_val, mode)
        if current_val < lowest_location:
            lowest_location = current_val
print(f"PART 2 LOWEST LOCATION: {lowest_location}")