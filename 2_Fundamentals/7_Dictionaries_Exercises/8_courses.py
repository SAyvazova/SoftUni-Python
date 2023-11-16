courses_and_participants = {}

command = input()
while command != "end":
    course_name, student_name = command.split(" : ")
    if course_name not in courses_and_participants:
        courses_and_participants[course_name] = []
    courses_and_participants[course_name].append(student_name)

    command = input()

for course, students in courses_and_participants.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")
