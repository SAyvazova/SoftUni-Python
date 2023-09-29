budget = 0

destination = input()

while destination != "End":

    min_needed_money = float(input())

    while budget < min_needed_money:
        saved_money = float(input())
        budget += saved_money
        if budget >= min_needed_money:
            print(f"Going to {destination}!")
            budget = 0
            break

    destination = input()