from hanoitower_rec import GraphicHanoi

def HanoiTower_iter(n, A, B, C):
    """solves the Hanoi tower problem (iterative way); shows every step that
    it needs to be done to move all disks from a source peg A to a target peg C
    with help of an auxiliary peg B"""
    
    step = 0
    if n == 0:
        return step
    names = {0: "A", 1: "B", 2: "C"}
    pegs = {0: A, 1: B, 2: C}
    print("START\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    GraphicHanoi(A, B, C, names)
    smallest = A[-1]
    while True:
        for k, p in enumerate(pegs.values()):
            if p == []:
                continue
            if smallest == p[-1]:
                s = k
        t = (s+1 if s < 2 else 0) if n%2 == 0 else (s-1 if s > 0 else 2)
        pegs[t].append(pegs[s].pop())
        step += 1
        print("step #{:03d}: move from {} to {}\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯".format(step, names[s], names[t]))
        GraphicHanoi(pegs[0], pegs[1], pegs[2], names)
        found = False
        for v in range (2, n+1):
            free = v
            for k, p in enumerate(pegs.values()):
                if p == []:
                    continue
                if free == p[-1]:
                    s = k
                    found = True
                    break
            if found == True:
                break
        if found == False:
            break
        i = [0, 1, 2]
        del i[s]
        if pegs[i[0]] == [] or pegs[i[1]] == []:
            t = i[0] if pegs[i[0]] == [] else i[1]
        else:
            t = i[0] if free < pegs[i[0]][-1] else i[1]
        pegs[t].append(pegs[s].pop()) 
        step += 1
        print("step #{:03d}: move from {} to {}\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯".format(step, names[s], names[t]))
        GraphicHanoi(pegs[0], pegs[1], pegs[2], names)
    return step

if __name__ == '__main__':
    num = int(input("Enter the number of disks >>"))
    A = [i for i in range(num, 0, -1)]
    B = []
    C = []
    numSteps = HanoiTower_iter(num, A, B, C)
    print("The number of steps is given by the formula 2^n-1")
    print("Theoretical number of steps: 2^{}-1 = {}".format(num, 2**num-1))
    print("Real number of steps: {}".format(numSteps))
    print("Are the values the same? {}".format(2**num-1 == numSteps))