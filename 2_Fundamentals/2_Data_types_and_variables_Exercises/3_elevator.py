from math import ceil

nr_people = int(input())
capacity_elevator = int(input())
nr_courses = ceil(nr_people / capacity_elevator)
print(nr_courses)
