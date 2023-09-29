nr_tabs = int(input())
salary = float(input())

for _ in range(nr_tabs):
    name = input()
    if name == "Facebook":
        salary -= 150
    elif name == "Instagram":
        salary -= 100
    elif name == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break

else:
    print(int(salary))