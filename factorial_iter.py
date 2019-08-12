def fac_iter(n):
    """returns a factorial (n!) of the natural number n (iterative way)"""
    
    assert isinstance(n, int), "The given number has to be integer!"
    assert n >= 0, "Factorial is defined for natural numbers!"
    n_factorial = 1
    for i in range(1, n+1):
        n_factorial *= i
    return n_factorial
