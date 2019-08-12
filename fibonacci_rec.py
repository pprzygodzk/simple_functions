def fib_rec(n):
    try:
        assert n > 0, "Fibonacci numbers are indexed from 1"
        if n == 1 or n == 2:
            return 1
        f_n = fib_rec(n-1) + fib_rec(n-2)
        return f_n
    except TypeError:
        print("Given argument is the wrong type!")
