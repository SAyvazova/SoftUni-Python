nr_inputs = int(input())
students = {}
for _ in range(nr_inputs):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)

for student, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.5:
        print(f"{student} -> {average_grade:.2f}")
