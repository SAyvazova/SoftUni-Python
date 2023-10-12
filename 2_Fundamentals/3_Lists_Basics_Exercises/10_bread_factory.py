max_energy = 100
energy = max_energy
coins = 100
events = input().split('|')

for event in events:
    event_parts = event.split('-')
    event_name_or_ingredient = event_parts[0]
    energy_or_coins = int(event_parts[1])

    if event_name_or_ingredient == 'rest':
        if energy + energy_or_coins <= max_energy:
            energy_gained = energy_or_coins
        else:
            energy_gained = max_energy - energy

        energy += energy_gained
        print(f"You gained {energy_gained} energy.")
        print(f"Current energy: {energy}.")

    elif event_name_or_ingredient == 'order':
        if energy >= 30:
            energy -= 30
            coins += energy_or_coins
            print(f"You earned {energy_or_coins} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if energy_or_coins <= coins:
            coins -= energy_or_coins
            print(f"You bought {event_name_or_ingredient}.")
        else:
            print(f"Closed! Cannot afford {event_name_or_ingredient}.")
            break

else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
