numbers = [int(number) for number in input().split(", ")]
positive_nums = [str(number) for number in numbers if number >= 0]
negative_nums = [str(number) for number in numbers if number < 0]
even_nums = [str(number) for number in numbers if number % 2 == 0]
odd_nums = [str(number) for number in numbers if number % 2 != 0]

print(f"Positive: {', '.join(positive_nums)}")
print(f"Negative: {', '.join(negative_nums)}")
print(f"Even: {', '.join(even_nums)}")
print(f"Odd: {', '.join(odd_nums)}")


