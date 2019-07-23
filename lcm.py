from nwd_iteracyjnie import NWD_iter
from functools import reduce

def LCM(a, b):
    """returns the least common multiple (LCM) of two integers a & b"""
    try:
        assert a > 0 and b > 0, "both arguments need to be different than zero"
        lcm = a*b/NWD_iter(a, b) # function NWD_iter is GCD (greatest common divisor)
        return lcm
    except TypeError:
        print("Given arguments are the wrong type!")
        

def LCM_n(*l):
    """returns the least common multiple of n integers: a1, a2, ..., an
    (recursive way)"""
    try:
        if len(l) == 2:
            return LCM(l[0], l[1])
        return reduce(LCM, l)
    except TypeError:
        print("Given arguments are the wrong type!")