def fibonacci_iter(n):
    try:
        assert n > 0, "Fibonacci numbers are indexed from 1"
        if n == 1 or n == 2:
            return 1
        f_1 = 1
        f_2 = 1
        for i in range(2, n):
            f_n = f_1 + f_2
            f_1 = f_2
            f_2 = f_n
        return f_n
    except TypeError:
        print("Given argument is the wrong type!")
