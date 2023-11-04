information = input()
students = {}
while ":" in information:
    name, ID, course = information.split(":")
    if course not in students:
        students[course] = {}
    students[course][ID] = name
    information = input()

course_to_search = " ".join(information.split("_"))
for course, student_info in students.items():
    if course == course_to_search:
        for ID, name in student_info.items():
            print(f"{name} - {ID}")
