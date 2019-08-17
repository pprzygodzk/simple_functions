import itertools as it

def IdentityMatrix(n):
    """builds an identity matrix I of a size n x n"""
    
    assert isinstance(n, int), "A size of a matrix needs to be integer!"
    KroneckerDelta = lambda i, j: int(i == j)
    for i in range(n):
        I = []
        for j in range(n):
            I.append(KroneckerDelta(i, j))
        yield I


def PrintArray(A, m):
    """prints the given array A in relation to the number m having the most digits
    (beautifying function)"""
    width = len(str(m))
    for i in range(len(A)):
        row = "["
        for j in range(len(A)):
            v = A[i][j]
            if j == len(A)-1:
                row += ("{:{w}d}".format(v, w = len(str(v)))) if len(str(v)) == width else ("  {:{w}d}".format(v, w = len(str(v))) if len(str(v)) == width-2 else " {:{w}d}".format(v, w = len(str(v))))
            elif j == 0:
                row += ("{:{w}d}, ".format(v, w = len(str(v)))) if len(str(v)) == width else ("{:{w}d},   ".format(v, w = len(str(v))) if len(str(v)) == width-2 else "{:{w}d},  ".format(v, w = len(str(v))))
            else:
                row += ("{:{w}d}, ".format(v, w = len(str(v)))) if len(str(v)) == width else (" {:{w}d},  ".format(v, w = len(str(v))) if len(str(v)) == width-2 else " {:{w}d}, ".format(v, w = len(str(v))))
        row += "]"
        print("{:^84}".format(row))


def SpiralMatrix(n, m = 0):
    """builds a spiral matrix S of a size n x n"""
    
    assert isinstance(n, int), "A size of a matrix needs to be integer!"
    S = [[0] * n for i in range(n)]
    distance = n
    i1, i2 = 0, -1
    
    for i, path in zip(it.cycle([1, 2]), it.cycle(["right", "down", "left", "up"])):
        if i == 2:
            distance -= 1
        if distance == 0:
            break
        for j in range(distance):
            m += 1
            if path == "right" or path == "left":
                i2 += 1 if path == "right" else -1
            else:
                i1 += 1 if path == "down" else -1
            S[i1][i2] = m
            
    PrintArray(S, m)
    return


def ZigZagMatrix(n, m = 1):
    """builds a zig-zag matrix Z of a size n x n"""
    
    assert isinstance(n, int), "A size of a matrix needs to be integer!"
    Z = [[0] * n for i in range(n)]
    i1, i2, c, a = 0, 0, 1, 1
    Z[0][0] = m
    distance = 0
    paths = ["right", "anti", "down", "anti"]
    
    while a != 2:
        for i, path in zip(it.cycle([1, 2]), it.cycle(paths)):
            if i == 2:
                distance += 1 if a == 1 else -1
                c *= -1
            if ((i1 == 0 and i2 == n-1 and n % 2 == 1) or (i1 == n-1 and i2 == 0 and n % 2 == 0)) and a == 1:
                a = 0
                break
            if i == 1:
                m += 1
                if path == "right":
                    i2 += 1
                else:
                    i1 += 1
                Z[i1][i2] = m
            else:
                for j in range(distance):
                    m += 1
                    i1 -= c
                    i2 += c
                    Z[i1][i2] = m
            if i1 == n-1 and i2 == n-1:
                a = 2
                break
        if n % 2 == 1:
            paths[0], paths[2] = paths[2], paths[0]
    
    PrintArray(Z, m)
    return
            

if __name__ == '__main__':
    print('************************************************************************************')
    print("{:^87}".format("IDENTITY MATRIX\n"))
    for row in IdentityMatrix(10):
        print("{:^87}".format(str(row)))
    print('************************************************************************************')
    print("{:^87}".format("SPIRAL MATRIX\n"))
    SpiralMatrix(10)
    print('************************************************************************************')
    print("{:^87}".format("ZIG-ZAG MATRIX\n"))
    ZigZagMatrix(10)
    print('************************************************************************************')