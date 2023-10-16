words = input().split()
palindrome = input()

all_palindromes_in_words = [word for word in words if word == word[::-1]]
specific_palindrome_count = all_palindromes_in_words.count(palindrome)

print(all_palindromes_in_words)
print(f"Found palindrome {specific_palindrome_count} times")
