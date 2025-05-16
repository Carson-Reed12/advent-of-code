import re
####### SETUP
with open("day1_input.txt", "r") as file:
    lines = file.readlines()

####### PART 1
total = 0
for line in [strip_line.strip() for strip_line in lines]:
    matches = re.findall("\d", line)

    if matches:
        total += int(f"{matches[0]}{matches[-1]}")

print(f"PART 1 TOTAL: {total}")

####### PART 2
def convertToInt(val):
    try:
        return int(val)
    except:
        if val == "one":
            return 1
        elif val == "two":
            return 2
        elif val == "three":
            return 3
        elif val == "four":
            return 4
        elif val == "five":
            return 5
        elif val == "six":
            return 6
        elif val == "seven":
            return 7
        elif val == "eight":
            return 8
        elif val == "nine":
            return 9
        elif val == "zero":
            return 0

total = 0
for line in [strip_line.strip() for strip_line in lines]:
    matches = re.findall("(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
    
    val1 = convertToInt(matches[0])
    val2 = convertToInt(matches[-1])

    total += int(f"{val1}{val2}")

print(f"PART 2 TOTAL: {total}")