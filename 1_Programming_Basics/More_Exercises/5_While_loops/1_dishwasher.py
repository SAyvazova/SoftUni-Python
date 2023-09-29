nr_bottles = int(input())
total_ml = 750 * nr_bottles
ml_used = 0
nr_clean_dishes = 0
nr_clean_pots = 0
nr_loads = 0

nr_dishes_or_pots = input()
while nr_dishes_or_pots != 'End':
    nr_dishes_or_pots = int(nr_dishes_or_pots)
    nr_loads += 1

    if nr_loads % 3 == 0:
        total_ml -= 15 * nr_dishes_or_pots
        nr_clean_pots += nr_dishes_or_pots
    else:
        total_ml -= 5 * nr_dishes_or_pots
        nr_clean_dishes += nr_dishes_or_pots

    if total_ml < 0:
        print(f"Not enough detergent, {abs(total_ml)} ml. more necessary!")
        break

    nr_dishes_or_pots = input()

else:
    if total_ml >= 0:
        print(f"Detergent was enough!")
        print(f"{nr_clean_dishes} dishes and {nr_clean_pots} pots were washed.")
        print(f"Leftover detergent {total_ml} ml.")



