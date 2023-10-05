number_1 = int(input())
number_2 = int(input())
operator = input()

result = 0
even_odd = ""
zero_flag = False

if operator == "+":
    result = number_1 + number_2

elif operator == "-":
    result = number_1 - number_2

elif operator == "*":
    result = number_1 * number_2

elif operator == "/":
    if number_2 == 0:
        zero_flag = True
    else:
        result = number_1 / number_2

elif operator == "%":
    if number_2 == 0:
        zero_flag = True
    else:
        result = number_1 % number_2


if operator in ["+", "-", "*"]:

    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"

    print(f"{number_1} {operator} {number_2} = {result} - {even_odd}")

elif operator == "/":
    if zero_flag:
        print(f"Cannot divide {number_1} by zero")
    else:
        print(f"{number_1} / {number_2} = {result:.2f}")

elif operator == "%":
    if zero_flag:
        print(f"Cannot divide {number_1} by zero")
    else:
        print(f"{number_1} % {number_2} = {result}")

