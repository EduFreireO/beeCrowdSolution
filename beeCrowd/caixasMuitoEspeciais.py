while True:
    try:
        def volume(array):
            return array[0] * array[1] * array[2]
        
        caixas, estoque = [int(a) for a in input().split()]
        if caixas == estoque == 0: break
        
        item = volume([int(a) for a in input().split()])
        dicionario = {}
        caixasValidas = []
        for caixa in range(estoque):
            dimensoes = volume([int(b) for b in input().split()])
            if dimensoes not in dicionario and dimensoes >= item:
                dicionario[dimensoes] = 1
            if dimensoes in dicionario:
                if dicionario[dimensoes] >= caixas and dimensoes not in caixasValidas :
                    caixasValidas.append(dimensoes)
                    continue
                dicionario[dimensoes] += 1
        if len(caixasValidas) > 0:
            print(min(caixasValidas) - item)
            continue
        print('impossible')
    
    except EOFError:
        break