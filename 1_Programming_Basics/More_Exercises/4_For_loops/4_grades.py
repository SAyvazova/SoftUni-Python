nr_students = int(input())
total_2 = 0
total_3 = 0
total_4 = 0
total_5= 0
total_grades = 0

for current_student in range(1, nr_students + 1):
    grade = float(input())
    total_grades += grade

    if 2 <= grade <= 2.99:
        total_2 += 1
    elif 3 <= grade <= 3.99:
        total_3 += 1
    elif 4 <= grade <= 4.99:
        total_4 += 1
    elif grade >= 5:
        total_5 += 1

average_grade = total_grades / nr_students
percentage_2 = total_2 / nr_students * 100
percentage_3 = total_3 / nr_students * 100
percentage_4 = total_4 / nr_students * 100
percentage_5 = total_5 / nr_students * 100


print(f"Top students: {percentage_5:.2f}%")
print(f"Between 4.00 and 4.99: {percentage_4:.2f}%")
print(f"Between 3.00 and 3.99: {percentage_3:.2f}%")
print(f"Fail: {percentage_2:.2f}%")
print(f"Average: {average_grade:.2f}")

