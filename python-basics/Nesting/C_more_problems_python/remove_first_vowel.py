def remove_first_vowel(s):
    vowels = "aeiou"
    result = ""
    removed = False
    for char in s:
        if char in vowels and not removed:
            removed = True
        else:
            result += char
    return result


print(remove_first_vowel("volcano"))
print(remove_first_vowel("celery"))
print(remove_first_vowel("juice"))
