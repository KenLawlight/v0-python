def choose_divisibles(numbers, target):
    result = []
    for num in numbers:
        if num % target == 0:
            result.append(num)
    return result

print(choose_divisibles([40, 7, 22, 20, 24], 4))
print(choose_divisibles([9, 33, 8, 17], 3))
print(choose_divisibles([4, 25, 1000], 10))
