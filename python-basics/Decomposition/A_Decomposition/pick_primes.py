def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def pick_primes(numbers):
    return [n for n in numbers if is_prime(n)]

print(pick_primes([12, 3, 7, 18, 11]))   
print(pick_primes([17, 23, 9, 42]))      
print(pick_primes([4, 2048, 100, 55]))   