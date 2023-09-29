name = input()

total_grades = 0
failed = 0
year = 0

while True:
    year_end_grade = float(input())

    if year_end_grade >= 4:
        year += 1
        total_grades += year_end_grade
    else:
        failed += 1

        if failed > 1:
            print(f"{name} has been excluded at {year + 1} grade")
            break

        continue #nqma smisul da sliza dolu- optimizaciq

    if year == 12:
        average_grade = total_grades / year
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break


## purvonachalnoto mi reshenie
# name = input()
#
# total_grades = 0
# failed = 0
# year = 0
#
# while True:
#     year_end_grade = float(input())
#
#     if year_end_grade >= 4:
#         year += 1
#         total_grades += year_end_grade #purvonachalno beshe na red 48 i togava ne raboteshe za poslednite 2 testa
#     else:
#         failed += 1
#
#     if year == 12:
#         average_grade = total_grades / year
#         print(f"{name} graduated. Average grade: {average_grade:.2f}")
#         break
#
#     elif failed > 1:
#         print(f"{name} has been excluded at {year + 1} grade")
#         break