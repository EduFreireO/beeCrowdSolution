while True:
    try:
        direito = []
        esquerdo = []
        pares = 0
        for a in range(int(input())):
            bota = input().split()
            bota[0] = int(bota[0])
            if bota[1] == 'D':
                direito.append(bota[0])
            else:
                esquerdo.append(bota[0])
        for b in direito:
            if b in esquerdo:
                esquerdo.remove(b)
                pares += 1
        print(pares)
    except EOFError:
        break