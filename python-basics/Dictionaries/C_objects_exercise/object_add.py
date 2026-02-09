def object_add(d1, d2):
    result = d1.copy()
    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result


obj1 = {"x": 3, "y": 10}
obj2 = {"y": 2, "x": 1}

print(object_add(obj1, obj2))


obj3 = {"a": 3, "b": 2, "c": -1}
obj4 = {"b": 5, "c": 1, "e": 4}

print(object_add(obj3, obj4))
