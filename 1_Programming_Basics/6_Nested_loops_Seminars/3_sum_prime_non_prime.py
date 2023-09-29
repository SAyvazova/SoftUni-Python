number = input()
prime_sum = 0
non_prime_sum = 0

while number != 'stop':
    number = int(number)
    non_prime_flag = False
    if number < 0:
        print("Number is negative.")
    else:
        nr_divider = 0
        for divider in range(2, number):
            if number % divider == 0:
                nr_divider += 1
                if nr_divider == 1:
                    non_prime_flag = True
                    break

        if non_prime_flag:
            non_prime_sum += number
        else:
            prime_sum += number

    number = input()

else:
    print(f"Sum of all prime numbers is: {prime_sum}")
    print(f"Sum of all non prime numbers is: {non_prime_sum}")
