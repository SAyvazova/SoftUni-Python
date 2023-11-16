legendary_items = {"shards": "Shadowmourne",
                   "fragments": "Valanyr",
                   "motes": "Dragonwrath"}

key_materials = {"shards": 0,
                 "fragments": 0,
                 "motes": 0}

junk_materials = {}

flag = False
while not flag:

    initial_input = input().split()

    for index in range(0, len(initial_input), 2):
        quantity = int(initial_input[index])
        material = initial_input[index + 1].lower()
        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                obtained_item = legendary_items[material]
                print(f"{obtained_item} obtained!")
                key_materials[material] -= 250
                flag = True
                break
        elif material not in junk_materials:
            junk_materials[material] = quantity
        else:
            junk_materials[material] += quantity


for material, quantity in key_materials.items():
    print(f"{material}: {quantity}")

for junk, quantity in junk_materials.items():
    print(f"{junk}: {quantity}")
