def censor_sentence(sentence, target_words):
    words = sentence.split()
    new_words = []

    for word in words:
        if word in target_words:
            new_words.append('*' * len(word))
        else:
            new_words.append(word)

    return " ".join(new_words)


print(censor_sentence('where the heck is my celery', ['heck','celery']))
print(censor_sentence('why you little sweetheart', ['sweetheart','salad']))