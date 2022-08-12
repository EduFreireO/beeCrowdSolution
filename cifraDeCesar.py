n = int(input())
while n > 0:
    string = input()
    pula = int(input())
    string = list(string.upper())
    alfabeto = []
    for orderAlfabetica in range(65, 91):
        alfabeto.append(chr(orderAlfabetica))
    for contador, letra in enumerate(string):
        string[contador] = alfabeto[(alfabeto.index(letra) - pula) % 26]
    print(''.join(string))
    n -= 1