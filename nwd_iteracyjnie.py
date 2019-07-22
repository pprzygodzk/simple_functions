def NWD_iter(a, b):
    try:
        assert a >= 0 and b > 0, "liczba a musi byc nieujemna, a b dodatnia"
        while b > 0:
            r = a % b
            a = b
            b = r
        return a
    except TypeError:
        print("Niewlasciwe argumenty dla funkcji")