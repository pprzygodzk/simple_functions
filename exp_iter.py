def exp_iter(a, n):
    """returns a to the nth power (iterative way)"""
    try:
        exp = 1
        if n > 0:
            for i in range(n):
                exp *= a
        if n < 0:
            for i in range(0, n, -1):
                exp *= 1/a
        return exp
    except TypeError:
        print("Given arguments are the wrong type!")
