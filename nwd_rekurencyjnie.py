def NWD(a, b):
    try:
        a = abs(int(a))
        b = abs(int(b))
        assert a >= b and b > 0, "a musi byc wieksze niz b, a b - dodatnie"
        return NWD_rek(a, b)
    except:
        print("Argumenty funkcji sa niewlasciwe")

def NWD_rek(a, b):
    if b == 0:
        return a
    return NWD_rek(b, a%b)