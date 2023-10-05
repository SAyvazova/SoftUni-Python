nr_jury = int(input())
presentation_name = input()
avg_grade_all = 0
nr_presentations = 0

while presentation_name != 'Finish':
    total_grade = 0
    nr_presentations += 1

    for current_grade in range(1, nr_jury + 1):
        grade = float(input())
        total_grade += grade

    avg_grade_presentation = total_grade / nr_jury
    avg_grade_all += avg_grade_presentation
    print(f"{presentation_name} - {avg_grade_presentation:.2f}.")

    presentation_name = input()

else:
    avg_grade_all /= nr_presentations
    print(f"Student's final assessment is {avg_grade_all:.2f}.")

