####### SETUP
with open("day1_input.txt", "r") as file:
    lines = file.readlines()

####### PART 1
calorie_groups = []
calories = 0
for line in lines:
    if line != "\n":
        calories += int(line.strip())
    else:
        calorie_groups.append(calories)
        calories = 0
calorie_groups.append(calories)

print(f"PART 1 MAX CALORIES: {max(calorie_groups)}")

####### PART 2
sum_calories = 0
for i in range(3):
    top_calories = max(calorie_groups)
    sum_calories += top_calories
    calorie_groups.remove(top_calories)
print(f"PART 2 TOP3 CALORIES: {sum_calories}")