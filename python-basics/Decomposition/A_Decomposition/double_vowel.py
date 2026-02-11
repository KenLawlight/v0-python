def double_vowel(s):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in s:
        if ch in vowels:
            result += ch * 2
        else:
            result += ch
    return result

print(double_vowel("runner"))
print(double_vowel("stoplight"))
print(double_vowel("gardener"))