v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

filled_up_volume = (p1 + p2) * h
percentage = filled_up_volume / v * 100
percentage_p1 = p1 / (p1 + p2) * 100
percentage_p2 = p2 / (p1 + p2) * 100

if percentage <= 100:
    print(f"The pool is {percentage:.2f}% full. Pipe 1: {percentage_p1:.2f}%. Pipe 2: {percentage_p2:.2f}%.")
else:
    diff = filled_up_volume - v
    print(f"For {h} hours the pool overflows with {diff:.2f} litters.")