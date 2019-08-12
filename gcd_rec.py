def GCD(a, b):
    """returns the greatest common divisor of two integers: a and b (recursive way)"""
    
    assert isinstance(a, int) and isinstance(b, int), "Both arguments have to be integer!"
    assert a >= 0 and b > 0, "Number a has to be greater than 0 / number b has to be positive!"
    return GCD_rec(a, b)

def GCD_rec(a, b):
    if b == 0:
        return a
    return GCD_rec(b, a%b)
