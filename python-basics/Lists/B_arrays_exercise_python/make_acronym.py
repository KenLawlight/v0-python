def make_acronym(sentence):
    return ''.join(word[0].upper() for word in sentence.split())

print(make_acronym("New York"))
print(make_acronym("same stuff different day"))
print(make_acronym("Laugh out loud"))
print(make_acronym("don't over think stuff"))
