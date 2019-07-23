def exp_rec(a, n):
    """returns a to the n-th power (recursive way)"""
    try:
        exp = 1
        if n > 0:
            exp = a * exp_rec(a, n-1)
        if n < 0:
            exp = (1/a) * exp_rec(a, n+1)
        return exp
    except TypeError:
        print("Given arguments are the wrong type!")
