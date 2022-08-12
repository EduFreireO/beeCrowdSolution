while True:
    try:
        quantidadeAmostras = int(input())
        if quantidadeAmostras == 0:
            break
        amostras = input()
        amostras = amostras.split()
        picos = 0
        quantidadeAmostras -= 1
        while quantidadeAmostras >= 0:
            amostras[quantidadeAmostras] = int(amostras[quantidadeAmostras])
            quantidadeAmostras -= 1
        for b in range(0, len(amostras)):
            if amostras[b - 1] < amostras[b] > amostras[(b + 1) % len(amostras)] or amostras[b - 1] > amostras[b] < amostras[(b + 1) % len(amostras)]:
                picos += 1
        print(picos)
    except EOFError:
        break