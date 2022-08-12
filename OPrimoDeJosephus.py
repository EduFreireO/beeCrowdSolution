while True:
    try:
        soldados = [a for a in range(1, int(input()) + 1)]
        primo = 1
        index = 1
        i = 2
        while len(soldados) > 1:
            soldados.pop((index + primo - 1 ) % len(soldados))
            primo += 1
            i = 2
            while i <= primo // 2:
                if primo % i == 0:
                    primo += 1
                    i = 2
                    continue
                i += 1
            index = (index + 1) % len(soldados)
        print(soldados[0])
    except EOFError:
        break