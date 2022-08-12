casos = int(input())
registro = {}
for caso in range(casos):
    texto = input()
    texto = texto.lower()
    for letra in texto:
        if letra not in registro:
            registro[letra] = 0
            continue
        registro[letra] += 1
print(registro)         