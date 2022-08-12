while True:
    try:
        hora1, minuto1, hora2, minuto2 = [int(a) for a in input().split()]
        if hora2 == 0:
            hora2 = 24
        if hora1 >= hora2 and minuto1 >= minuto2:
            print((24 + hora2 % 12 - hora1% 12)*60 - (minuto1 - minuto2))
        else:
            print((hora2 - hora1)*60 + (minuto2 - minuto1))
    except EOFError:
        break