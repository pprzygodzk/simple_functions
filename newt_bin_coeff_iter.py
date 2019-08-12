from factorial_iter import fac_iter

def Newt_bin_coeff_iter(n, k):
    """returns a value of a Newton binomial coefficient for given n & k
    (iterative way)"""
    
    assert isinstance(n, int) and isinstance(k, int), "Both arguments have to be integer!"
    assert k >= 0 and k <= n, "Arguments out of range!"
    coefficient = fac_iter(n) / (fac_iter(k) * fac_iter(n-k))
    return coefficient
