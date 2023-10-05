initial_score = int(input())

initial_bonus_points = 0

if initial_score <= 100:
    initial_bonus_points = 5
elif 100 < initial_score < 1000:
    initial_bonus_points = 0.2 * initial_score
elif initial_score > 1000:
    initial_bonus_points = 0.1 * initial_score

# if number <= 100:
#     bonus_points = 5
# elif number <= 1000:
#     bonus_points = number * 0.2
# else:
#     bonus_points = number * 0.1


# if number % 2 == 0:
#     bonus_points = bonus_points + 1
#
# if number % 10 == 5:
#     bonus_points = bonus_points + 2
#
# print(bonus_points)
# print(number + bonus_points)
additional_bonus_points = 0

if initial_score % 2 == 0:
    additional_bonus_points = 1
elif initial_score % 10 == 5:
    additional_bonus_points = 2
# tuk tova e udachno, zashtoto nqma kak edno chislo da e i chetno, i da zavurshva na 5
# no, ako primerno se iskashe da zavurshi na 4, togava trqbva da se izpolzva if i za dvete proverki, zashtoto edno chislo,
# koeto zavurshva na 4 e sushto chetno
bonus_points = initial_bonus_points + additional_bonus_points
final_score = initial_score + initial_bonus_points + additional_bonus_points

print(bonus_points)
print(final_score)

