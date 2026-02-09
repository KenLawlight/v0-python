def secret_cipher(s, mapping):
    result = ""
    for char in s:
        if char in mapping:
            result += mapping[char]
        else:
            result += "?"
    return result


print(secret_cipher("jello", {"j":"r","l":"s","e":"i"}))
print(secret_cipher("lantern", {"e":"o","l":"p","n":"m","r":"j"}))
