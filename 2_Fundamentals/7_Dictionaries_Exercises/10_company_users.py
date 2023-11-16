companies_and_employees = {}
command = input()
while command != "End":
    company_name, employee_id = command.split(" -> ")
    if company_name not in companies_and_employees:
        companies_and_employees[company_name] = []

    if employee_id not in companies_and_employees[company_name]:
        companies_and_employees[company_name].append(employee_id)

    command = input()

for company, employees in companies_and_employees.items():
    print(f"{company}")
    for employee in employees:
        print(f"-- {employee}")
