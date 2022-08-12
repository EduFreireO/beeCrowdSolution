while True:
    try:
        entrada = int(input())
        while entrada > 0 :
            a, b = input().split()
            if b in a[len(a) - len(b):]:
                print('encaixa')
            else:
                print('nao encaixa')
            entrada -= 1
    except EOFError:
        break