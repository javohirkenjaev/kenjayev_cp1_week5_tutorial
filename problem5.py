days = int(input('Enter the number of days: '))
measures = []
for days in range(days):
    m = int(input('Enter the measurment for next day: '))
    measures.append(m)

for i in range(days):
    print(f"Day {i+1}: {measures[i]} cm")

print(f"First height: {measures[0]} cm")
print(f"Last height: {measures[-1]} cm")
print(f"Chage {measures[-1] - measures[0]}")