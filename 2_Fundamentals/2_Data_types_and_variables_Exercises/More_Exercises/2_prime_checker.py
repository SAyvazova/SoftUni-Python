num = int(input())
for divisor in range(2, num):
    if num % divisor == 0:
        print("False")
        break

else:
    print("True")