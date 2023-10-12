fire_level = input().split('#')
water_available = int(input())
effort = 0
cells_put_out = []

for fire_cell in fire_level:
    fire_cell_elements = fire_cell.split(' = ')
    fire_type = fire_cell_elements[0]
    water_needed = int(fire_cell_elements[1])

    if water_needed > water_available:
        continue

    if fire_type == 'High':
        if 81 <= water_needed <= 125:
            water_available -= water_needed
            effort += 0.25 * water_needed
            cells_put_out.append(water_needed)
    elif fire_type == 'Medium':
        if 51 <= water_needed <= 80:
            water_available -= water_needed
            effort += 0.25 * water_needed
            cells_put_out.append(water_needed)
    elif fire_type == 'Low':
        if 1 <= water_needed <= 50:
            water_available -= water_needed
            effort += 0.25 * water_needed
            cells_put_out.append(water_needed)

print("Cells:")
for cell in cells_put_out:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(cells_put_out)}")
