while True:
    try:
        num = input()
        cutoff = float(input())
        parteInteira = int(float(num))
        if '.' in num and num.index('.') < len(num) - 1:
            numFracionaria = float(num[num.index('.') : ])
            if numFracionaria > cutoff:
                parteInteira += 1
            print(parteInteira)
        else:
            print(parteInteira)
            continue
    except EOFError:
        break


