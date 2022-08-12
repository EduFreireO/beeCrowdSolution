while True:
    try:
        # Recebimento das entradas.
        numeroDeCartas = [int(n) for n in input().split()]
        alice = [int(a) for a in input().split()]
        beatriz = [int(b) for b in input().split()]

        # Remoção das cartas repetidas
        for i in alice:
            while alice.count(i) > 1:
                alice.remove(i)
        for c in beatriz:
            while beatriz.count(c) > 1:
                beatriz.remove(c)

        # Parte principal. Contagem das trocas
        def trocaDeCartas(deck1, deck2):
            trocaMenor = 0
            trocaMaior = 0
            for carta in deck1:
                if carta not in deck2:
                    trocaMenor += 1
            for carta in deck2:
                if carta not in deck1:
                    trocaMaior += 1
            if trocaMaior > trocaMenor:
                return trocaMenor

            return trocaMaior


        trocas = trocaDeCartas(alice, beatriz)
        print(trocas)
    except EOFError:
        break