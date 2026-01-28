def lengthiest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) >= len(longest):
            longest = word
    return longest

print(lengthiest_word("I am pretty hungry"))
print(lengthiest_word("we should think outside of the box"))
print(lengthiest_word("down the rabbit hole"))
print(lengthiest_word("simmer down"))
