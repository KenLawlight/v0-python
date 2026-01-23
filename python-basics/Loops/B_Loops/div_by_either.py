def div_by_either(num1, num2, max_num):
    for i in range(1, max_num):
        if i % num1 == 0 or i % num2 == 0:
            print(i)

div_by_either(4, 3, 16)
