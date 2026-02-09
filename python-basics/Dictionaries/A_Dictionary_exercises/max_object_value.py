def max_object_value(d):
    max_key = None
    max_val = None
    for key, val in d.items():
        if max_val is None or val > max_val:
            max_key = key
            max_val = val
    return [max_key, max_val]


print(max_object_value({"a": 5, "b": 2, "c": 6, "d": 7, "e": 4}))
print(max_object_value({"lychee": 11, "rambutan": 13, "papaya": 9}))
