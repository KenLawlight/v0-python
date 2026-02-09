def shorten_long_words(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []
    for word in words:
        if len(word) > 4:
            new_word = ""
            for char in word:
                if char not in vowels:
                    new_word += char
            result.append(new_word)
        else:
            result.append(word)
    return " ".join(result)


print(shorten_long_words("they are very noble people"))
print(shorten_long_words("stick with it"))
print(shorten_long_words("ballerina, you must have seen her"))
