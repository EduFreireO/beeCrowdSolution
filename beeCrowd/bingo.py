from math import fabs
while True:
    try:
        tamanhoDaCarte = [int(a) for a in input().split()]
        if tamanhoDaCarte[0] == tamanhoDaCarte[1] == 1:
            break
        bolas = [int(b) for b in input().split()]
        sub = set()
        for i in range(len(bolas) - 1):
            for j in range(i,len(bolas)):
               sub.add(int(fabs(bolas[i] - bolas[j])))
        if len(sub) == tamanhoDaCarte[0] + 1:
            print('Y')
        else:
            print('N')
    except EOFError:
        break

