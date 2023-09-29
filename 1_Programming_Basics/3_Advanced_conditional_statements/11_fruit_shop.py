fruit = str(input())
day_of_week= str(input())
quantity = float(input())

fruit_price = 0
wrong_input = False

if day_of_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
   if fruit == "banana":
        fruit_price = 2.5
   elif fruit == "apple":
       fruit_price = 1.2
   elif fruit == "orange":
       fruit_price = 0.85
   elif fruit == "grapefruit":
       fruit_price = 1.45
   elif fruit == "kiwi":
       fruit_price = 2.7
   elif fruit == "pineapple":
       fruit_price = 5.5
   elif fruit == "grapes":
       fruit_price = 3.85
   else:
       wrong_input = True

elif day_of_week in [ "Saturday", "Sunday"]:
    if fruit == "banana":
        fruit_price = 2.7
    elif fruit == "apple":
        fruit_price = 1.25
    elif fruit == "orange":
        fruit_price = 0.9
    elif fruit == "grapefruit":
        fruit_price = 1.6
    elif fruit == "kiwi":
        fruit_price = 3
    elif fruit == "pineapple":
        fruit_price = 5.6
    elif fruit == "grapes":
        fruit_price = 4.2
    else:
        wrong_input = True

else:
    wrong_input = True


if wrong_input == True:
    print("error")

elif wrong_input == False:
    total_price = quantity * fruit_price
    print(f"{total_price:.2f}")
