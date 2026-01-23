def total(numbers):
    sum_total = 0
    for num in numbers:
        sum_total += num
    return sum_total

print(total([3, 2, 8]))
print(total([-5, 7, 4, 6]))
print(total([7]))
print(total([]))
