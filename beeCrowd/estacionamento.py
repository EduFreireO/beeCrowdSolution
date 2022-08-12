while True:
    try:
        comprimento, eventos =  [int(b) for b in input().split()]
        dicionario = {}
        valor = 0
        while eventos > 0:
            entrada = input().split()
            acao = entrada[0]
            placa = entrada[1]
            if len(entrada) >= 3 and int(entrada[2]) > comprimento:
                eventos -= 1
                continue
            if acao == 'C':
                tamanho = int(entrada[2])
                valor += 10
                comprimento -= tamanho
                dicionario[placa] = tamanho
                eventos -= 1
                continue
            comprimento += dicionario[placa]
            eventos -= 1
        print(valor)
    except EOFError:
        break


