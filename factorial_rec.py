def fac_rec(n):
    """returns a factorial (n!) of the natural number n (recursive way)"""
    
    assert isinstance(n, int), "Given argument has to be integer!"
    assert n >= 0, "Factorial is defined for natural numbers!"
    if n == 0:
        return 1
    n_factorial = n * fac_rec(n-1)
    return n_factorial
