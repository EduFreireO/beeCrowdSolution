while True:
    try:
        frase = input()
        if frase == '*':
            break
        frase = (frase.lower()).split()
        tautograma = True
        for palavra in frase:
            if frase[0][0] != palavra[0]:
                tautograma = False
                print('N')
                break
        if tautograma == True:
            print('Y')
    except EOFError:
        break            
