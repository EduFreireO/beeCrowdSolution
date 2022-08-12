while True:
    try:
        corridas, pilotos = [int(a) for a in input().split()]
        if corridas == pilotos == 0: break
        posicoes = []
        contaPiloto = 0
        pontos = [0 for v in range(pilotos)]
        for corrida in range(corridas):
            aux = [int(b) for b in input().split()]
            posicoes.append(aux)
        n = int(input())
        while n > 0:
            sistema = [int(c) for c in input().split()]
            for corrida in range(corridas):
                for piloto in range(pilotos):
                    if posicoes[corrida][piloto] <= sistema[0]:
                        pontos[piloto] +=  sistema[posicoes[corrida][piloto]]
            maiorNumero = pontos[0]
            c = []
            for contador,j in enumerate(pontos):
                if j > maiorNumero:
                    maiorNumero = j
                    c.clear()
                    c.append(contador + 1)
                elif j == maiorNumero:
                    c.append(contador + 1)
            i = 0
            while i < len(c):
                c[i] = str(c[i])
                i += 1
            print(' '.join(c))
            pontos = [0 for v in range(pilotos)]
            n -= 1
    except EOFError:
        break