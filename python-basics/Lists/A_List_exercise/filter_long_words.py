def filter_long_words(words):
    return [word for word in words if len(word) < 5]

print(filter_long_words(["kale", "cat", "retro", "axe", "heirloom"]))
print(filter_long_words(["disrupt", "pour", "trade", "pic"]))
