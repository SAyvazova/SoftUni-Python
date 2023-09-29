budget = float(input())
nr_video_card = int(input())
nr_processor = int(input())
nr_RAM = int(input())

total_price_video_cards = nr_video_card * 250
price_processor = total_price_video_cards * 0.35
price_RAM = total_price_video_cards * 0.1

total_price = total_price_video_cards + (nr_processor * price_processor) + (nr_RAM * price_RAM)

if nr_video_card > nr_processor:
    total_price = total_price * 0.85

diff = abs(budget-total_price)

if budget >= total_price:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")

# Изход
# На конзолата се отпечатва 1 ред, който трябва да изглежда по следния начин:
# •	Ако бюджета е достатъчен:
# "You have {остатъчен бюджет} leva left!"
# •	Ако сумата надхвърля бюджета:
# "Not enough money! You need {нужна сума} leva more!"
# Резултатът да се форматира до втория знак след десетичната запетая.
