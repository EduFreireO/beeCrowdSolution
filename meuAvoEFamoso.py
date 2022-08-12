while True:
    try:
        rankings, jogadores = [int(a) for a in input().split()]
        if rankings == jogadores == 0: break
        registro = {}
        for ranking in range(rankings):
            grid = [int(b) for b in input().split()]
            for jogador in range(jogadores):
                if grid[jogador] in registro:
                    registro[grid[jogador]] += 1
                else:
                    registro[grid[jogador]] = 1
        #Pede para retornar a tupla de identificacao do jogador e sua posicao separadamente
        valores = list(registro.values())
        valores.remove(max(valores))
        newHigher = max(valores)
        x = []
        for key,value in registro.items():
            if value == newHigher:
                x.append(key)
        x = [str(a) for a in  sorted(x)]
        print(' '.join(x)+ ' ')


    except EOFError:
        break