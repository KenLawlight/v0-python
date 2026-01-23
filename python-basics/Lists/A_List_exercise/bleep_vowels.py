def bleep_vowels(text):
    vowels = "aeiouAEIOU"
    return ''.join('*' if c in vowels else c for c in text)

print(bleep_vowels("skateboard"))
print(bleep_vowels("slipper"))
print(bleep_vowels("range"))
print(bleep_vowels("brisk morning"))
