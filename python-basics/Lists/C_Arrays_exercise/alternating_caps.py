def alternating_caps(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if i % 2 == 0:
            words[i] = words[i].lower()
        else:
            words[i] = words[i].upper()
    return ' '.join(words)

print(alternating_caps("take them to school"))
print(alternating_caps("What did ThEy EAT before?"))
