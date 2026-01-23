def divisors(num):
    return [i for i in range(1, num + 1) if num % i == 0]

print(divisors(15))
print(divisors(7))
print(divisors(24))
