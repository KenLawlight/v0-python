def find_char_positions(text, char):
    for i in range(len(text)):
        if text[i] == char:
            print(i)

find_char_positions("banana", "a")

