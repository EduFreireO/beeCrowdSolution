# Crise de energia. Resolução de Eduardo Oliveira.
while True:
    try:
        entrada = int(input())
        if entrada == 0:
            break
        regioes = [n for n in range(1,entrada + 1)]
        copia = regioes[:]
        salto = 0
        index = 0
        while len(copia) >= 1:
            copia.pop(index)
            index = (index + salto) % len(copia)
            if len(copia) == 1 and copia[0] == 13:
                salto += 1
                break
            if len(copia) == 1:
                copia = regioes[:]
                index = 0
                salto += 1

        print(salto)

    except:
        break
