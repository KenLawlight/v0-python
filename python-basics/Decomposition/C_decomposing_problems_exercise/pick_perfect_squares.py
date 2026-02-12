def pick_perfect_squares(nums):
    perfects = []
    
    for n in nums:
        root = int(n ** 0.5)
        if root * root == n:
            perfects.append(n)
    
    return perfects


print(pick_perfect_squares([6,4,81,21,36]))
print(pick_perfect_squares([100,24,144]))
print(pick_perfect_squares([30,25]))