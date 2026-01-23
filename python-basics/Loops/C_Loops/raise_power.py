def raise_power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

print(raise_power(2, 5))
print(raise_power(4, 3))
print(raise_power(10, 4))
print(raise_power(7, 2))
