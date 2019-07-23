from silnia_iteracyjnie import silnia_iter

def Newt_bin_coeff_iter(n, k):
    """returns a value of a Newton binomial coefficient for given n & k
    (iterative way)"""
    try:
        assert k >= 0 and k <= n, "Arguments out of range!"
        coefficient = silnia_iter(n) / (silnia_iter(k) * silnia_iter(n-k)) # silnia_iter is a function for factorial
        return coefficient
    except TypeError:
        print("Given arguments are the wrong type!")