def your_average_function(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

print(your_average_function([5, 2, 7, 24]))
print(your_average_function([100, 6]))
print(your_average_function([31, 32, 40, 12, 33]))
print(your_average_function([]))
