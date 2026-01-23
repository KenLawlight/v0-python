def in_range(start, end, num):
    return start <= num <= end

print(in_range(5, 13, 8))
print(in_range(5, 13, 29))
print(in_range(100, 125, 100))
print(in_range(100, 125, 99))
print(in_range(40, 45, 44))
print(in_range(40, 45, 45))
print(in_range(40, 45, 46))
