resources_dict = {}
while True:
    current_resource = input()
    if current_resource == "stop":
        break

    current_quantity = int(input())
    if current_resource not in resources_dict:
        resources_dict[current_resource] = 0
    resources_dict[current_resource] += current_quantity

for resource, quantity in resources_dict.items():
    print(f"{resource} -> {quantity}")
