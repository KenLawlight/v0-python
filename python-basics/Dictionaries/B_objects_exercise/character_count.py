def character_count(s):
    result = {}
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


print(character_count("evening"))
print(character_count("mississippi"))
print(character_count("chili"))
