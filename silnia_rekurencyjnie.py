def silnia_rekurencja(n):
    try:
        assert n >= 0, "silnia moze byc tylko z liczb nieujemnych"
        if n == 0:
            return 1
        n_silnia = n * silnia_rekurencja(n-1)
        return n_silnia
    except TypeError:
        print("Niewlasciwy argument dla funkcji")