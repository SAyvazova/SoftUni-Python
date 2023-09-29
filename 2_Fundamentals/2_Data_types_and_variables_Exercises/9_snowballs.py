nr_snowballs = int(input())
best_snowball_weight = 0
best_snowball_time = 0
best_snowball_quality = 0
best_snowball_value = 0
for current_snowball in range(1, nr_snowballs + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight / time) ** quality
    if value > best_snowball_value:
        best_snowball_weight = weight
        best_snowball_time = time
        best_snowball_quality = quality
        best_snowball_value = int(value)

print(f"{best_snowball_weight} : {best_snowball_time} = {best_snowball_value} ({best_snowball_quality})")