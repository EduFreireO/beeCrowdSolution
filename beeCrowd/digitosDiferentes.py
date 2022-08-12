#Utilizar o dict para guardar a referencia ao numero. Alem disso, guardar a decomposicao em uma set
while True:
    try:
        n, m = [int(a) for a in input().split()]
        invalidos = 0
        decomposicao = {}
        for j in range(n, m+1):
            aux = j
            decomposicao[aux] = set()
            while j > 0:
                if j % 10 in decomposicao[aux]:
                    invalidos += 1
                    break
                decomposicao[aux].add(j % 10)
                j //= 10
        print((m - n + 1) - invalidos)
    except EOFError:
        break