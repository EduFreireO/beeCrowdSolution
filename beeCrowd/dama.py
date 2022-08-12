while True:
    try:
        coordenadas = [int(a) for a in input().split()] #Linha e coluna.
        diagonalPonto = coordenadas[3] - coordenadas[2]
        if coordenadas[0] == 0:
            continue
        xPonto = coordenadas[2]
        yPonto = coordenadas[3]
        operacao = 0
        if xPonto == coordenadas[0] and yPonto == coordenadas[1]:
            print('0')
            continue
        while diagonalPonto > coordenadas[1] - coordenadas[0]:
            xPonto += 1
            yPonto -= 1
            diagonalPonto -= 2
        while diagonalPonto < coordenadas[1] - coordenadas[0]:
            xPonto -= 1
            yPonto +=1
            diagonalPonto += 2
        if xPonto == coordenadas[0] and yPonto == coordenadas[1]:
            print('1')
            break
        # Testa linhas e colunas
        if coordenadas[0] != coordenadas[2]:
            operacao += 1
        if coordenadas[1] != coordenadas[3]:
            operacao += 1
        print(operacao)
    except EOFError:
        break

