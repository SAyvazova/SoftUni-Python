nr_goes = int(input())
points = 0
total_0_9 = 0
total_10_19 = 0
total_20_29 = 0
total_30_39 = 0
total_40_50 = 0
total_invalid = 0

for _ in range (nr_goes):
    number = int(input())

    if 0 <= number <= 9:
        points += 0.2 * number
        total_0_9 += 1

    elif 10 <= number <= 19:
        points += 0.3 * number
        total_10_19 += 1

    elif 20 <= number <= 29:
        points += 0.4 * number
        total_20_29 += 1

    elif 30 <= number <= 39:
        points += 50
        total_30_39 += 1

    elif 40 <= number <= 50:
        points += 100
        total_40_50 += 1
    else:
        points /= 2
        total_invalid += 1

percentage_0_9 = total_0_9 / nr_goes * 100
percentage_10_19 = total_10_19 / nr_goes * 100
percentage_20_29 = total_20_29 / nr_goes * 100
percentage_30_39 = total_30_39 / nr_goes * 100
percentage_40_50 = total_40_50 / nr_goes * 100
percentage_invalid = total_invalid / nr_goes * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {percentage_0_9:.2f}%")
print(f"From 10 to 19: {percentage_10_19:.2f}%")
print(f"From 20 to 29: {percentage_20_29:.2f}%")
print(f"From 30 to 39: {percentage_30_39:.2f}%")
print(f"From 40 to 50: {percentage_40_50:.2f}%")
print(f"Invalid numbers: {percentage_invalid:.2f}%")