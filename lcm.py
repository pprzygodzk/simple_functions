from gcd_iter import GCD_iter
from functools import reduce

def LCM(a, b):
    """returns the least common multiple (LCM) of two integers a & b"""
    
    assert isinstance(a, int) and isinstance(b, int), "Given arguments have to be integer!"
    assert a > 0 and b > 0, "Both arguments need to be different than zero"
    lcm = a*b/GCD_iter(a, b)
    return int(lcm)
        

def LCM_n(*l):
    """returns the least common multiple of n integers: a1, a2, ..., an
    (recursive way)"""
    
    try:
        if len(l) == 2:
            return LCM(l[0], l[1])
        return reduce(LCM, l)
    except TypeError:
        print("Given arguments are the wrong type!")
