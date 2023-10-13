def is_palindrome(integer: str) -> bool:
    if integer == integer[::-1]:
        return True
    return False


list_integers = input().split(", ")
for number in list_integers:
    print(is_palindrome(number))
