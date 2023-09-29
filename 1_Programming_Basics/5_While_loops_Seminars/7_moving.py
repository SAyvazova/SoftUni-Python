width = int(input())
length = int(input())
height = int(input())

area = width * length * height
no_more_space = False

nr_boxes = input()

while nr_boxes != "Done":
    nr_boxes = int(nr_boxes)
    area -= nr_boxes

    if area <= 0:
        no_more_space = True
        break

    nr_boxes = input()

if no_more_space:
    print(f"No more free space! You need {abs(area)} Cubic meters more.")
else:
    print(f"{area} Cubic meters left.")