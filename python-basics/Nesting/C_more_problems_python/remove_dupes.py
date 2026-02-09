def remove_dupes(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


print(remove_dupes(["x", "y", "y", "x", "z"]))
print(remove_dupes([False, False, True, False]))
print(remove_dupes([42, 5, 7, 42, 7, 3, 7, 7]))
