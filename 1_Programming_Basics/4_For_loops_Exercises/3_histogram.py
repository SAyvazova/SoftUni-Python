nr_numbers = int(input())

count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0

# count_p1, count_p2, count_p3, count_p4, count_p5 = 0, 0, 0, 0, 0

for _ in range(1, nr_numbers + 1):
    current_number = int(input())
    if current_number < 200:
        count_p1 += 1
    elif 200 <= current_number <= 399:
        count_p2 += 1
    elif 400 <= current_number <= 599:
        count_p3 += 1
    elif 600 <= current_number <= 799:
        count_p4 += 1
    elif current_number >= 800:
        count_p5 += 1


p1 = (count_p1/nr_numbers) * 100
p2 = (count_p2/nr_numbers) * 100
p3 = (count_p3/nr_numbers) * 100
p4 = (count_p4/nr_numbers) * 100
p5 = (count_p5/nr_numbers) * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")