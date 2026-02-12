def lala_language(sentence):
    vowels = "aeiou"
    words = sentence.split()
    new_words = []

    for word in words:
        if len(word) <= 3:
            new_words.append(word)
        else:
            new_word = ""
            for char in word:
                if char in vowels:
                    new_word += char + "l" + char
                else:
                    new_word += char
            new_words.append(new_word)

    return " ".join(new_words)


print(lala_language('this is pretty strange'))
print(lala_language('can you speak our language'))