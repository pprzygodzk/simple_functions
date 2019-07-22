def silnia_iter(n):
    try:
        assert n >= 0, "silnia moze byc tylko z liczb nieujemnych"
        n_silnia = 1
        for i in range(1, n+1):
            n_silnia *= i
        return n_silnia
    except TypeError:
        print("Niewlasciwy argument dla funkcji")
