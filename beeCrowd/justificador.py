espaco = False
while True:
    try:
        palavras = int(input())
        if palavras == 0 : break
        lista = []
        maior = 0
        for palavra in range(palavras):
            aux = input()
            lista.append(aux)
            if len(aux) > maior: maior = len(aux)
        if espaco == True: print('')
        for elemento in lista:
            print(' '*(maior - len(elemento))+elemento)
        espaco = True
    except:
        EOFError