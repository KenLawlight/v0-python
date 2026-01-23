def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

print(is_palindrome("level"))
print(is_palindrome("Race car"))
print(is_palindrome("python"))
