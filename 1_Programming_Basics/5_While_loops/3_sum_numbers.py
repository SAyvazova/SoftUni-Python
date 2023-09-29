NUMBER = int(input())
sum_numbers = 0

while True:
    number = int(input())
    sum_numbers += number

    if sum_numbers >= NUMBER:
        print(sum_numbers)
        break


