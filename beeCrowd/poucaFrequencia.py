while True:
    try:
        for i in range(int(input())):
            estudantes = int(input())
            alunos = input().split()
            chamada = input().split()
            reprovados = []
            for estudante in range(estudantes):
                ausencia = chamada[estudante].count('A')
                medico = chamada[estudante].count('M')
                quantAulas = len(chamada[estudante])
                if ausencia / (quantAulas - medico) > 0.25:
                    reprovados.append(alunos[estudante])
            reprovados = ' '.join(reprovados)
            print(reprovados)
            continue
    except EOFError:
        break