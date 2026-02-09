def letter_map(s, mapping):
    result = ""
    for char in s:
        if char in mapping:
            result += mapping[char]
        else:
            result += char
    return result


print(letter_map("symbolic", {"y": "i", "o": "a", "c": "k"}))
print(letter_map("colossal", {"o": "x", "s": "p"}))
print(letter_map("miniscule", {"u": "t", "i": "f", "e": "q"}))
