def factorial_division(num1, num2):
    factorial_num1 = num1
    for multiplier in range(1, num1):
        factorial_num1 *= multiplier

    factorial_num2 = num2
    for multiplier2 in range(1, num2):
        factorial_num2 *= multiplier2

    return factorial_num1 / factorial_num2


number1 = int(input())
number2 = int(input())

print(f"{factorial_division(number1, number2):.2f}")