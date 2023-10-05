name_actor = input()
initial_points = float(input())
nr_evaluators = int(input())

total_points = initial_points

for _ in range(nr_evaluators):
    name_evaluator = input()
    points_evaluator = float(input())
    total_points += (len(name_evaluator) * points_evaluator) / 2

    if total_points > 1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!")
        break

else:
    diff = 1250.5 - total_points
    print(f"Sorry, {name_actor} you need {diff:.1f} more!")