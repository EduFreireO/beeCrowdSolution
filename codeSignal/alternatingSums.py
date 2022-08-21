def solution(a):
    tamanho = len(a)
    somador = 0
    for j in range(0, len(a), 2):
        somador += a[j]
    return [somador, sum(a) - somador]