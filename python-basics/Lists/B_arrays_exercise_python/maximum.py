def maximum(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for num in numbers[1:]:
        if num > max_value:
            max_value = num
    return max_value

print(maximum([5, 6, 3, 7]))
print(maximum([17, 15, 19, 11, 2]))
print(maximum([]))

