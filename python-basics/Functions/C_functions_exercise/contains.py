def contains(text, sub):
    return sub.lower() in text.lower()

print(contains("caterpillar", "pill"))
print(contains("lion's share", "on"))
print(contains("SORRY", "or"))
print(contains("tangent", "gem"))
print(contains("clock", "ok"))

