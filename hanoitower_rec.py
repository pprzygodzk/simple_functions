def GraphicHanoi(A, B, C, names = ["A", "B", "C"]):
    """shows graphically the current state of pegs"""
    h = max(len(A), len(B), len(C))

    if h-1 >= len(A):
        A = A + [" " for j in range(len(A), h)]
    if h-1 >= len(B):
        B = B + [" " for k in range(len(B), h)]
    if h-1 >= len(C):
        C = C + [" " for l in range(len(C), h)] 

    for i in range(h-1, -1, -1):
        print("{:^8}{:^8}{:^8}".format(A[i], B[i], C[i]))
    print(" __|___  __|___  __|___ ")        
    print("[{:^6}][{:^6}][{:^6}]".format(names[0], names[1], names[2]))
    print("\n\n")
    return

def GraphicHanoiFixOrder(A, B, C, names):
    """fixes the names of pegs which are constantly changing as a result of function calls"""
    if names == ["A", "B", "C"]:
        GraphicHanoi(A, B, C)
    elif names == ["A", "C", "B"]:
        GraphicHanoi(A, C, B)
    elif names == ["B", "A", "C"]:
        GraphicHanoi(B, A, C)
    elif names == ["B", "C", "A"]:
        GraphicHanoi(C, A, B)
    elif names == ["C", "A", "B"]:
        GraphicHanoi(B, C, A)
    elif names == ["C", "B", "A"]:
        GraphicHanoi(C, B, A)

def HanoiTower(n, A, B, C, names = ["A", "B", "C"], step = 0):
    """solves the Hanoi tower problem; shows every step that
    it needs to be done to move all discs from a source peg A to a target peg B
    with help of an auxiliary peg C (recursive way)"""

    if n >= 1:
        step = HanoiTower(n-1, A, C, B, [names[0], names[2], names[1]], step)
        B.append(A.pop())
        step += 1
        print("step #{:03d}: move from {} to {}\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯".format(step, names[0], names[1]))
        GraphicHanoiFixOrder(A, B, C, names)
        step = HanoiTower(n-1, C, B, A, [names[2], names[1], names[0]], step)
        return step
    return step

if __name__ == '__main__':
    num = int(input("Enter the number of disks >>"))
    A = [i for i in range(num, 0, -1)]
    B = []
    C = []
    print("START\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    GraphicHanoi(A, B, C, names = ["A", "B", "C"])
    numSteps = HanoiTower(num, A, B, C)
    print("The number of steps is given by the formula 2^n-1")
    print("Theoretical number of steps: 2^{}-1 = {}".format(num, 2**num-1))
    print("Real number of steps: {}".format(numSteps))
    print("Are the values the same? {}".format(2**num-1 == numSteps))