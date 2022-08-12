genome = 1
while True:
    try:
        def inverteElementos(lista, begin, end):
            for i in range((end - begin + 1)//2):
                lista[begin], lista[end] = lista[end], lista[begin]
                begin += 1
                end -= 1
            return lista
        gene = int(input())
        if gene == 0: break
        gene = [int(i) for i in range(1, gene + 1)]
        inversoes = int(input())
        for inversao in range(inversoes):
            inicio, fim  = [int(b) for b in input().split()]
            gene = inverteElementos(gene, inicio - 1, fim - 1)
        print(f'genome {genome}')
        for consulta in range(int(input())):
            base = int(input())
            print(gene.index(base) + 1)
        genome += 1
    except EOFError:
        break