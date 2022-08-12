n = int(input())
c = 0
while(c < n):
    string = list(input())
    metadeDaString = len(string)//2 - 1
    for letra in range(0, metadeDaString//2 + 1):
        letraDireita = string[metadeDaString]
        letraEsquerda = string[letra]
        string[letra] = letraDireita
        string[metadeDaString] = letraEsquerda
        metadeDaString -= 1
    metadeDaString = len(string)//2
    tamanhoDaString = len(string) - 1
    for letra in range(0, (metadeDaString//2)):
        letraEsquerda = string[metadeDaString + letra]
        letraDireita = string[tamanhoDaString]
        string[metadeDaString + letra] = letraDireita
        string[tamanhoDaString] = letraEsquerda
        tamanhoDaString -= 1;
    string = ''.join(string)
    print(string)
    c+=1
