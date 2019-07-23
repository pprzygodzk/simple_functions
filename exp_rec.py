def exp_rec(a, n):
    """returns a to the n-th power (recursive way)"""
    try:
        if n == 0:
            return 1
        elif n > 0:
            exp = a * exp_rec(a, n-1)
            return exp
        else:
            exp = (1/a) * exp_rec(a, n+1)
            return exp
    except TypeError:
        print("Given arguments are the wrong type!")