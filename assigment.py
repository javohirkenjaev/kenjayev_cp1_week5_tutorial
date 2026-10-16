def classify(value):
    if value < 1998:
        return "Below range"
    elif 1998 <= value <= 2002:
        return "In range"
    else:
        return "Above range"
def calculate_average(total, count):
    return total / count

flour_bags = int(input("Enter the number of flour bags: "))
total_weight = 0
below_range_count = 0
in_range_count = 0
above_range_count = 0

for i in range(flour_bags):
    bag_weight = int(input("Enter the flour bag weight: "))

    classification = classify(bag_weight)
    print(classification)
    
    if classification == "Below range":
        below_range_count += 1
    elif classification == "In range":
        in_range_count += 1
    else:
        above_range_count += 1

average_weight = calculate_average(total_weight, flour_bags)
print(f"Total weight: {total_weight} g")
print(f"Average weight: {average_weight} g")
print(f"Below range: {below_range_count}")
print(f"In range: {in_range_count}")
print(f"Above range: {above_range_count}")