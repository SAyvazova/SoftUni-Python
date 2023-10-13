from math import sqrt, floor


def closest_to_center_of_two(X1, Y1, X2, Y2):
    distance1 = sqrt(X1 ** 2 + Y1 ** 2)
    distance2 = sqrt(X2 ** 2 + Y2 ** 2)

    if distance1 <= distance2:
        print(f"({floor(X1)}, {floor(Y1)})")
    else:
        print(f"({floor(X2)}, {floor(Y2)})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

closest_to_center_of_two(x1, y1, x2, y2)