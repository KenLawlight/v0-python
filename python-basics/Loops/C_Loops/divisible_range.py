def divisible_range(min_val, max_val, num):
    for i in range(min_val + 1, max_val):
        if i % num == 0:
            print(i)

divisible_range(17, 40, 9)
divisible_range(10, 24, 4)
