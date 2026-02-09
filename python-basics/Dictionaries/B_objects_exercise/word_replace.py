def word_replace(sentence, replacements):
    words = sentence.split()
    result = []
    for word in words:
        if word in replacements:
            result.append(replacements[word])
        else:
            result.append(word)
    return " ".join(result)


print(word_replace(
    "I never take naps during the day",
    {"never": "always", "day": "weekend"}
))

print(word_replace(
    "the park is closed",
    {"closed": "open", "the": "a"}
))

print(word_replace(
    "I do what I want",
    {"I": "we", "cat": "dog"}
))

