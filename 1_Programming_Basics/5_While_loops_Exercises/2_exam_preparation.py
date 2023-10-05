nr_bad_grades_to_stop = int(input())
total_grades = 0
nr_exercises = 0
bad_grades_counter = 0
last_name_exercise = ''

name_exercise = input()

while name_exercise != "Enough":
    grade = float(input())

    if grade <= 4:

        bad_grades_counter += 1

        if bad_grades_counter == nr_bad_grades_to_stop:
            print(f"You need a break, {bad_grades_counter} poor grades.")
            break


    last_name_exercise = name_exercise
    total_grades += grade
    nr_exercises += 1

    name_exercise = input()

else:
    average_grade = total_grades / nr_exercises
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {nr_exercises}")
    print(f"Last problem: {last_name_exercise}")
