def count_vowels(text):
    return sum(1 for char in text.lower() if char in "aeiou")

print(count_vowels("hello"))
print(count_vowels("Programming"))
