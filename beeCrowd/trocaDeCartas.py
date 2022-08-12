while True:
    try:
        # Recebimento das cartas
        quantidadeDeCartas = [int(q) for q in input().split()]
        alice = [int(a) for a in input().split()]
        beatriz = [int(b) for b in input().split()]

        # Sets são os conjuntos. Aqueles mesmos da matematica!
        alice = set(alice)      # Uma caracteristica interessante dos sets
        beatriz = set(beatriz)  # é a de que ele excluem elementos repetidos.

        # metodo difference te da a subtração dos conjuntos!
        aliceDiference = alice.difference(beatriz) # Equivalente a fazer (set(alice) - set(beatriz))
        beatrizDiference = beatriz.difference(alice)

        # Resolução propriamente dita
        if len(aliceDiference) >= len(beatrizDiference):
            print(len(beatrizDiference))
        else:
            print(len(aliceDiference))

    except EOFError:
        break