def Newt_bin_coeff_rec(n, k):
    """returns a value of a Newton binomial coefficient for given n & k
    (recursive way)"""
    try:
        assert k >= 0 and k <= n, "Arguments out of range!"
        if k == 0 or k == n:
            return 1
        coefficient = Newt_bin_coeff_rec(n-1, k-1) + Newt_bin_coeff_rec(n-1, k)
        return coefficient
    except TypeError:
        print("Given arguments are the wrong type!")