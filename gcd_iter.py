def GCD_iter(a, b):
    """returns the greatest common divisor of two integers: a and b"""
    
    assert isinstance(a, int) and isinstance(b, int), "Given arguments have to be integer!"
    assert a > 0 and b > 0, "Given numbers have to be greater than 0!"
    
    while b > 0:
        r = a % b
        a = b
        b = r
    return a
