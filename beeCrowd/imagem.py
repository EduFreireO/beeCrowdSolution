# entrada : altura e largura originais.
# altura linhas --> desenho
# altura e largura finais.
altura, largura = [int(a) for a in input().split()]
desenho = []
desenhoRed = []
line = []
for linha in range(altura):
    desenho.append(input())

alturaFinal, larguraFinal = [int(b) for b in input().split()]
for coluna in range(altura):
    for linha in range(0, largura):
        line.append(desenho[coluna][linha] * )
