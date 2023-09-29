import math

record_in_sec = float(input())
distance_in_meters = float(input())
time_in_sec_per_meter = float(input())

individual_time = distance_in_meters * time_in_sec_per_meter

if distance_in_meters >= 15:
    individual_time = individual_time + 12.5 * (math.floor(distance_in_meters/15))

if individual_time < record_in_sec:
    print(f" Yes, he succeeded! The new world record is {individual_time:.2f} seconds.")
else:
    diff = individual_time - record_in_sec
    print(f"No, he failed! He was {diff:.2f} seconds slower.")