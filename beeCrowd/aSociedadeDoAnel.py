while True:
    try:
        numero = int(input())
        dicionario = {'A': 0 , 'E': 0, 'H': 0, 'M':0, 'X':0}

        for elemento in range(numero):
            ser = input().split()[1]
            if ser in dicionario:
                dicionario[ser] += 1
        bichos = [
            ('Hobbit(s)',dicionario['X']),
            ('Humano(s)',dicionario['H']),
            ('Elfo(s)',dicionario['E']), 
            ('Anao(s)',dicionario['A']), 
            ('Mago(s)',dicionario['M'])
            ]
        for bicho in bichos:
            print(f'{bicho[1]} {bicho[0]}')
        print('\n')   
    except EOFError:
        break        

    
