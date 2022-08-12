def solution(n):
    n = list(str(n))
    primeiraMetade = sum(map(int,n[ : (len(n))//2 ]))
    segundaMetade = sum(map(int,n[len(n)//2: ]) )
    if primeiraMetade == segundaMetade:
        return True
    return False
solution(1230)
