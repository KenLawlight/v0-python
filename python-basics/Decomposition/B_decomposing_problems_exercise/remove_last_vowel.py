def remove_last_vowel(s):
    vowels = "aeiouAEIOU"
    for i in range(len(s) - 1, -1, -1):
        if s[i] in vowels:
            return s[:i] + s[i+1:]
    return s

print(remove_last_vowel("speaker"))
print(remove_last_vowel("trading"))
print(remove_last_vowel("thunder"))
print(remove_last_vowel("myth"))