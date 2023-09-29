change = float(input())
remaining = change
nr_coins = 0

while remaining > 0:

    if remaining - 2 >= 0:
        remaining -= 2

    elif remaining - 1 >= 0:
        remaining -= 1

    elif remaining - 0.5 >= 0:
        remaining = round(remaining - 0.5, 2)

    elif remaining - 0.2 >= 0:
        remaining = round(remaining - 0.2, 2)

    elif remaining - 0.1 >= 0:
        remaining = round(remaining - 0.1, 2)

    elif remaining - 0.05 >= 0:
        remaining = round(remaining - 0.05, 2)

    elif remaining - 0.02 >= 0:
        remaining = round(remaining - 0.02, 2)

    elif remaining - 0.01 >= 0:
        remaining = round(remaining - 0.01, 2)

    nr_coins += 1

else:
    print(nr_coins)


#reshenie na lektorkata
# change = float(input())
# remaining = change * 100
# nr_coins = 0
#
# while remaining > 0:
#
#     if remaining - 200 >= 0:
#         remaining -= 200
#
#     elif remaining - 100 >= 0:
#         remaining -= 100
#
#     elif remaining - 50 >= 0:
#         remaining -= 50
#
#     elif remaining - 20 >= 0:
#         remaining -= 20
#
#     elif remaining - 10 >= 0:
#         remaining -= 10
#
#     elif remaining - 5 >= 0:
#         remaining -= 5
#
#     elif remaining - 2 >= 0:
#         remaining -= 2
#
#     elif remaining - 1 >= 0:
#         remaining -= 1
#
#     else:
#         break #za input -0.56 dade greshka zaradi rabota s floatnati chisla (0.56 * 100 - 56.0...1) i za tova restoto
#                nikoga ne se zanulqva. Tq go reshi po tozi nachin
#
#     nr_coins += 1
#
# print(nr_coins) #tuka ne moje else kum while, zashtoto ako navlezne v red 69, nqma da printira nishto