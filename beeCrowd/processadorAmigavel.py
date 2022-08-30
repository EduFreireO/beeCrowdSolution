while True:
    try:
        numero =list(input().lower())
        valido = ['l','o',',',' ']


        for digito in numero:
            if digito not in valido and not digito.isdigit():
                numero = ''.join(numero)
                break
            # Horrivel
            if ord(digito) == 32 or digito == ',':
                numero.remove(digito)
                continue
            if digito == 'l':
                numero[numero.index(digito)] = '1'
                continue
            if digito == 'o':
                numero[numero.index(digito)] = '0'
                continue

        numero = ''.join(numero)
        if not numero.isdigit():
            print('error')
            continue
        numero = int(numero)
        if numero < 2147483647:
            print(numero)
            continue
        print('error')
    except EOFError:
        break
