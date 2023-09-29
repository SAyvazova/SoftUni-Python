a = int(input())
b = int(input())
max_generated = int(input())
nr_generated = 0
for A in range(35,56):
    for B in range(64,97):
        for x in range(1, a + 1):
            for y in range(1, b + 1):
                print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")