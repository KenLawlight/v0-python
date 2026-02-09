def spam(pairs):
    result = []
    for pair in pairs:
        word = pair[0]
        count = pair[1]
        for i in range(count):
            result.append(word)
    return " ".join(result)


array1 = [["hi", 3], ["bye", 2]]
print(spam(array1))

array2 = [["cat", 1], ["dog", 2], ["bird", 4]]
print(spam(array2))
