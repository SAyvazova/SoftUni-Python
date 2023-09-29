number = int(input())
nr_solutions = 0

for x1 in range(0, number + 1): # = range(number + 1)
    for x2 in range(0, number + 1):
        for x3 in range(0, number + 1):
            if x1 + x2 + x3 == number:
                nr_solutions += 1

print(nr_solutions)

# trugnah da go pravq s maxsize, no realno kogato chisloto stane ravno na n, nie imame edno validno reshenie i nqma
# smisul ot chislata sled tova

