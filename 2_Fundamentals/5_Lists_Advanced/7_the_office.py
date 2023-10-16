from statistics import mean


def office_happiness_calculations():
    employees_happiness = list(map(int, input().split()))
    improvement_factor = int(input())
    improved_happiness = [happiness * improvement_factor for happiness in employees_happiness]
    average_happiness = mean(improved_happiness)
    happy_count = len([happiness for happiness in improved_happiness if happiness >= average_happiness])
    total_count = len(employees_happiness)

    return happy_count, total_count


happy_employees_count, total_count_employees = office_happiness_calculations()

if happy_employees_count >= total_count_employees / 2:
    print(f"Score: {happy_employees_count}/{total_count_employees}. Employees are happy!")
else:
    print(f"Score: {happy_employees_count}/{total_count_employees}. Employees are not happy!")
