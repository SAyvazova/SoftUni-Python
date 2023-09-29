number = int(input())

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if all(number % x == 0 for x in (a, b, c, d)):
                    print(f"{a}{b}{c}{d}", end=" ")
