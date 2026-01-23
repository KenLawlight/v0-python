def stay_positive(numbers):
    return [num for num in numbers if num > 0]

print(stay_positive([10, -4, 3, 6]))
print(stay_positive([-5, 11, -40, 30.3, -2]))
print(stay_positive([-11, -30]))
