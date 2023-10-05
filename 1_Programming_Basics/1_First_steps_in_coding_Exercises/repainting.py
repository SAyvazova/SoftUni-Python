square_meters_nylon = int(input())
liters_paint= int(input())
liters_paint_thinner = int(input())
hours_need_to_finish = int(input())

total_price_nylon = (square_meters_nylon + 2) * 1.5
total_price_paint = (liters_paint * 1.1) * 14.5
total_price_paint_thinner = liters_paint_thinner * 5
bag_price = 0.4

total_price_materials = total_price_nylon + total_price_paint + total_price_paint_thinner + bag_price
payment_to_workers_per_hour = total_price_materials * 0.3

total_price_repainting = total_price_materials + payment_to_workers_per_hour * hours_need_to_finish

print(total_price_repainting)




