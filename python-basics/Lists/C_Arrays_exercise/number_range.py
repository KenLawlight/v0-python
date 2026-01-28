def number_range(min_val, max_val, step):
    result = []
    current = min_val
    while current <= max_val:
        result.append(current)
        current += step
    return result

print(number_range(10, 40, 5))
print(number_range(14, 24, 3))
print(number_range(8, 35, 6))
