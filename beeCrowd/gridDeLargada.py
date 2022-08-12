while True:
    try:
        nPilotos = int(input())
        largada = [int(a) for a in input().split()]
        chegada = [int(b) for b in input().split()]
        ultrapassagens = 0
        for index in range(nPilotos):
            posLargada = largada.index(chegada[index])
            if posLargada > index:
                ultrapassagens += posLargada - index
                continue
            if posLargada == index:
                anteriores = chegada[:index]
                for j in range(0,index):
                    if largada[j] not in anteriores:
                        ultrapassagens += 1
        print(ultrapassagens)
    except EOFError:
        break





