def remove_last_vowel(s):
    vowels = "aeiouAEIOU"
    for i in range(len(s) - 1, -1, -1):
        if s[i] in vowels:
            return s[:i] + s[i+1:]
    return s

def trendy_text(sentence):
    words = sentence.split()
    return " ".join(remove_last_vowel(word) for word in words)

print(trendy_text("the concert will be epic"))
print(trendy_text("breakfast food is wonderful"))
print(trendy_text("the weather will improve hopefully"))