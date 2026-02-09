def element_quantities(d):
    result = []
    for key in d:
        for i in range(d[key]):
            result.append(key)
    return result


quantities1 = {"cat": 3, "bird": 1, "dog": 2}
print(element_quantities(quantities1))

quantities2 = {"blue": 3, "brown": 1}
print(element_quantities(quantities2))
