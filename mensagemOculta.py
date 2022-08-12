for i in range(int(input())):
    string = input()
    contador = []
    permitido = True
    for letra in string:
        if letra != ' ' and permitido == True:
            contador.append(letra)
            permitido = False
            continue
        if letra == ' ':
            permitido = True
    print(''.join(contador))            
   
