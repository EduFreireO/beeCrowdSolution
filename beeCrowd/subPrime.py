while True:
    try:
        banks, debentures = [int(a) for a in input().split()]
        if banks == debentures == 0:
            break
        reserve = [int(b) for b in input().split()]
        devedor = False
        while debentures > 0:
            transacoes = [int(c) for c in input().split()]
            reserve[transacoes[0] - 1] -= transacoes[2]
            reserve[transacoes[1] - 1] += transacoes[2]
            debentures -= 1
        for i in reserve:
            if i < 0:
                devedor = True
                break
        if devedor == True:
            print('N')
            continue
        print('S')
    except EOFError:
        break