# A Lenda de Flavious Josephus
casos = int(input())
case = 1
while casos > 0:
    quantidade, salto = [int(a) for a in input().split()]
    soldados = [b for b in range(1, quantidade + 1)]
    salto -= 1
    index = salto % len(soldados)
    while len(soldados) > 1:
        soldados.pop(index)
        index = (index + salto) % len(soldados)
    print(f'Case {case}: {soldados[0]}')
    case +=1
    casos -= 1
