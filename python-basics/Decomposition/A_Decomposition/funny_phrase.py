def double_vowel(s):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in s:
        if ch in vowels:
            result += ch * 2
        else:
            result += ch
    return result

def funny_phrase(sentence):
    words = sentence.split()
    return " ".join(double_vowel(word) for word in words)

print(funny_phrase("she dreamed of being a runner"))
print(funny_phrase("park near the stoplight"))
print(funny_phrase("we need many gardeners"))