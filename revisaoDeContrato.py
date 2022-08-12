while True:
    try:
        digito, valor = input().split()
        if digito == '0' and valor == '0':
            break
        valor = list(valor)
        while valor.count(digito) != 0:
            valor.remove(digito)
        if valor.count(0) == len(valor):
            print(0)
        else:
            numero = int(''.join(valor))
            print(numero)
    except EOFError:
        break