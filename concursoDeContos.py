# BEE 1222. A lógica utiliza : contar a quantidade de linhas.
while True:
    try:
            # Inicialização das entradas.
        entradas = input()  # Número de páginas, Linhas por página, e Char por linha.
        conto = input()
        entradas = [int(n) for n in entradas.split(' ')]

            # Variaveis utilizadas durante o programa
        salto = int(entradas[2]) # entradas[2] = Char por linha
        inicioLinha = 0
        fimLinha = salto - 1
        linhas = 0
        linhasPorPagina = int(entradas[1])
        if fimLinha != len(conto) - 1:

                # Contagem das linhas.
            while fimLinha != len(conto) - 1:

                # Delimita o fim de uma linha. sendo um espaço em branco, ou o fim de uma palavra.
                while conto[fimLinha] != ' ':
                    if conto[fimLinha + 1] == ' ':
                        break
                    fimLinha -= 1
                linhas += 1
                inicioLinha = fimLinha + 1

                # Não faz sentido que o primeiro char de uma linha seja um espaço.
                if conto[inicioLinha] == ' ':
                    inicioLinha += 1
                    fimLinha += 1
                fimLinha += salto

                if fimLinha >= len(conto) - 1:
                    linhas+= 1
                    break
            if linhas % linhasPorPagina != 0 :
                print(linhas // linhasPorPagina + 1)
            else:
                print(linhas // linhasPorPagina)
        else:
            print(1)

    except EOFError:
        break