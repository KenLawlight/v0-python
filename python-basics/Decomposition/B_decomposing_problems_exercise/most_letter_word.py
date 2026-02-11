def most_letter_word(sentence, char):
    words = sentence.split()
    max_count = -1
    best_word = ""
    
    for word in words:
        count = word.count(char)
        if count > max_count:
            max_count = count
            best_word = word
            
    return best_word

print(most_letter_word('she received an award for excellence in science','e'))
print(most_letter_word('she received an award for excellence in science','a'))
print(most_letter_word('I hope sophomore year comes soon','o'))
print(most_letter_word('I hope sophomore year comes soon','s'))