def loading_bar(percentage):
    count_percentage_signs = percentage // 10
    count_points = 10 - count_percentage_signs
    if count_percentage_signs in range(0, 10):
        return f"{percentage}% [{count_percentage_signs * '%'}{count_points * '.'}]\nStill loading..."
    elif percentage == 100:
        return "100% Complete!\n[%%%%%%%%%%]"


loaded_percentage = int(input())
print(loading_bar(loaded_percentage))