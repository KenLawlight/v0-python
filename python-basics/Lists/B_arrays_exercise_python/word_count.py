def word_count(sentence, target_words):
    count = 0
    for word in sentence.split():
        if word in target_words:
            count += 1
    return count

print(word_count("open the window please", ["please", "open", "sorry"]))
print(word_count("drive to the cinema", ["the", "driver"]))
print(word_count("can I have that can", ["can", "I"]))

