def multiplication_type(num1: int, num2: int, num3: int) -> str:
    list_nums = [num1, num2, num3]
    if 0 in list_nums:
        result = "zero"
    else:
        negative_counter = 0
        for num in list_nums:
            if num < 0:
                negative_counter += 1

        if negative_counter % 2 == 0:
            result = "positive"
        else:
            result = "negative"

    return result


number1 = int(input())
number2 = int(input())
number3 = int(input())

print(multiplication_type(number1, number2, number3))
