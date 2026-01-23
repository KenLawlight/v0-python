def string_size(text):
    if len(text) < 5:
        return "small"
    elif len(text) == 5:
        return "medium"
    else:
        return "large"

print(string_size("cat"))
print(string_size("bell"))
print(string_size("ready"))
print(string_size("shirt"))
print(string_size("shallow"))
print(string_size("intelligence"))
