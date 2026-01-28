def common_elements(arr1, arr2):
    return [item for item in arr1 if item in arr2]

print(common_elements(["a", "c", "d", "b"], ["b", "a", "y"]))
print(common_elements([4, 7], [32, 7, 1, 4]))
