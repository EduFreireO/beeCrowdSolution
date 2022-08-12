while True:
    try:
        string1 = input()
        string2 = input()
        def subString(menorString,maiorString):
            subString = 0
            ultima = 1
            for contador in range(len(menorString)):
                while ultima <= len(menorString) and menorString[contador : ultima] in maiorString:
                    if ultima - contador > subString:
                        subString  = ultima - contador
                    ultima += 1
                ultima = contador + 1
            return  subString
        if len(string1) > len(string2):
            resposta = subString(string2,string1)
        else:
            resposta = subString(string1,string2)

        print(resposta)
    except EOFError:
        break