period = int(input())

nr_doctors = 7
total_patients = 0
treated_patients = 0

for current_day in range(1, period + 1):
    if current_day % 3 == 0:
        if untreated_patients > treated_patients:
            nr_doctors += 1

    nr_patiens_per_day = int(input())
    total_patients += nr_patiens_per_day

    if nr_patiens_per_day < nr_doctors:
        treated_patients += nr_patiens_per_day
    else:
        treated_patients += nr_doctors

    untreated_patients = total_patients - treated_patients


print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
