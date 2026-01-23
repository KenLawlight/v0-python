def one_or_none(a, b):
    return a != b

print(one_or_none(False, False))
print(one_or_none(True, False))
print(one_or_none(False, True))
print(one_or_none(True, True))

