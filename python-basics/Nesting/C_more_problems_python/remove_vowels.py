def remove_vowels(s):
    result = ""
    for char in s:
        if char not in "aeiou":
            result += char
    return result


print(remove_vowels("jello"))
print(remove_vowels("sensitivity"))
print(remove_vowels("cellar door"))
