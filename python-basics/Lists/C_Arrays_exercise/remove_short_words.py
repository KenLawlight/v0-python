def remove_short_words(sentence):
    return ' '.join(word for word in sentence.split() if len(word) >= 4)

print(remove_short_words("knock on the door will you"))
print(remove_short_words("a terrible plan"))
print(remove_short_words("run faster that way"))
