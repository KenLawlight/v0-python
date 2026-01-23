def num_odds(numbers):
    count = 0
    for num in numbers:
        if num % 2 != 0:
            count += 1
    return count

print(num_odds([4, 7, 2, 5, 9]))
print(num_odds([11, 31, 58, 99, 21, 60]))
print(num_odds([100, 40, 4]))
