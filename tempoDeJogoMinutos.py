horaInicial, minInicial, horaFinal, minFinal = input().split()
horaInicial = int(horaInicial)
minInicial = int(minInicial)
horaFinal = int(horaFinal)
minFinal = int(minFinal)

if minInicial > minFinal:
    minTotal = 60 - minInicial - minFinal
else:
    minTotal = minFinal - minInicial
if horaInicial == horaInicial:
    horaTotal = 0
else:

print(f'O JOGO DUROU {} HORA(S) E {minTotal} MINUTO(S)')