import math

figure_type = input()
area = 0

if figure_type == "square":
    a = float(input())
    area = a ** 2

elif figure_type == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b

elif figure_type == "circle":
    r = float(input())
    area = r ** 2 * math.pi

elif figure_type == "triangle":
    a = float(input())
    b = float(input())
    area = (a * b) / 2

print(f"{area: .3f}")
