while True:
    try:
        casosDeTeste = int(input())
        for caso in range(casosDeTeste):
            frase = list(input())
            j = 0
            for index,j in enumerate(frase):
                if not j.isalpha():
                    frase.pop(index)
            conjunto = set(frase)
            if len(conjunto) == 26:
                print('frase completa')
                continue
            if len(conjunto) >= 13:
                print('frase quase completa')
                continue
            print('frase mal elaborada')
    except EOFError:
        break