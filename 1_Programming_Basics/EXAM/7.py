n = int(input())
total_sum = 0
product = 1
is_found = False

for a in range(1, 10):
    for b in range(9, a - 1, -1):
        for c in range(0, 10):
            for d in range(9, c - 1, -1):

                total_sum = a + b + c + d
                product = a * b * c * d

                if total_sum == product and n % 10 == 5:
                    print(f'{a}{b}{c}{d}')
                    is_found = True
                    break
                elif (product // total_sum) == 3 and n % 3 == 0:
                    print(f'{d}{c}{b}{a}')
                    is_found = True
                    break

            if is_found:
                break

        if is_found:
            break

    if is_found:
        break

else:
    print('Nothing found')
