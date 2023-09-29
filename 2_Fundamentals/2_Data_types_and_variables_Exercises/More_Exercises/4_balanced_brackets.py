nr_lines = int(input())
opening_bracket_counter = 0
closing_bracket_counter = 0
last_bracket_type = ""
opening_bracket = "("
closing_bracket = ")"

for _ in range(nr_lines):
    received_input = input()
    if (last_bracket_type == "" and received_input == closing_bracket) or last_bracket_type == received_input:
        print("UNBALANCED")
        break

    if received_input == opening_bracket:
        opening_bracket_counter += 1
        last_bracket_type = opening_bracket
    elif received_input == closing_bracket:
        closing_bracket_counter += 1
        last_bracket_type = closing_bracket

else:
    if opening_bracket_counter == closing_bracket_counter:
        print("BALANCED")
    else:
        print("UNBALANCED")
