caso = int(input())
while caso > 0:
    primeira, segunda = input().split()
    def combinador(string1, string2):
        array = []
        if len(string1) > len(string2):
            tamanho = len(string2)
            stringMaior = string1
        else:
            tamanho = len(string1)
            stringMaior = string2
        for i in range(tamanho):
            array.append(string1[i])
            array.append(string2[i])
        return ''.join(array) + stringMaior[tamanho:]
    caso -= 1
    var = combinador(primeira, segunda)
    print(var)
