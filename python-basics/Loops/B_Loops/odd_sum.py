def odd_sum(max_num):
    total = 0
    for i in range(1, max_num + 1, 2):
        total += i
    return total

print(odd_sum(10))
print(odd_sum(5))

