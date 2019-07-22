def fib_rekur(n):
    try:
        assert n > 0, "liczenie wyrazow ciagu fibonacciego zaczyna sie od 1"
        if n == 1 or n == 2:
            return 1
        f_n = fib_rekur(n-1) + fib_rekur(n-2)
        return f_n
    except TypeError:
        print("Niewlasciwy argument dla funkcji")