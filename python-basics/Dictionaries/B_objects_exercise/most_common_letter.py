def most_common_letter(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    max_count = 0
    max_char = ""
    for char, count in counts.items():
        if count > max_count:
            max_count = count
            max_char = char
    return max_char


print(most_common_letter("building"))
print(most_common_letter("shoestring"))
print(most_common_letter("preparedness"))
