def fizz_buzz(max_num):
    for i in range(1, max_num + 1):
        if (i % 3 == 0) != (i % 5 == 0):
            print(i)

fizz_buzz(18)
fizz_buzz(33)
