while True:
    try:
        alunos, jantares = [int(b) for b in input().split()]
        if alunos == jantares == 0 : break
        planilha = []
        for i in range(alunos):
            planilha.append(True)
        while jantares > 0:
            presenca = [int(c) for c in input().split()]
            i = 0
            while i < alunos:
                if presenca[i] == 0:
                    planilha[i] = False
                i += 1
            jantares -= 1
        if True in planilha:
            print('yes')
            continue
        print('no')
    except EOFError:
        break