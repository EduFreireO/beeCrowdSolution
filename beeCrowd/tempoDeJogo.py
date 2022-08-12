inicio, final = input().split()
inicio = int(inicio)
final = int(final)
if(inicio == final):
    print('O JOGO DUROU 24 HORA(S)')
else:
    print(f'O JOGO DUROU {final % 12 + 12 - inicio % 12 } HORA(S)')