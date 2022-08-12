#Entrada : N, M ---> Numero de caixas que o cliente deseja comprar, Quantidade de caixas no estoque.
# 2) Dimensões do produto do cliente.
# 3) M dimensões ---> Dimensoes das caixas no estoque.

# O cliente que caixas iguais que se encaixem perfeitamente na dimensão especificada
# Entretanto ---> Pode não haver caixas desse tamanho suficientes. Para isso, ele deseja utilizar caixas
# que o tamanho seja o menor possivel, mas que ainda sim, possam  armazenar o item na dimensão especificada

# Calcular o volume das caixas do estoque.
# Depois ---> Procurar as dimesões que possue pelo menos N caixas e retirar a menor dentre elas
while True:
    try:
        def volume(array):
            return array[0] * array[1] * array[2]
        caixas, estoque = input().split()
        if caixas == estoque == 0: break
        caixas = int(caixas)
        estoque = int(estoque)
        item = volume([int(a) for a in input().split()])
        dicionario = {}
        x = []
        for caixa in range(estoque):
            dimensoes = volume([int(b) for b in input().split()])
            if dimensoes not in dicionario and dimensoes >= item:
                dicionario[dimensoes] = 1
            if dimensoes in dicionario:
                if dicionario[dimensoes] >= caixas and dimensoes not in x:
                    x.append(dimensoes)
                    continue
                dicionario[dimensoes] += 1
        if len(x) > 0:
            print(min(x) - item)
            continue
        print('impossible')
    except EOFError:
        break