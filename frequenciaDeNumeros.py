quantidade = int(input())
ocorrencias = {}
array = []

def insertionSort(array):
    for i in range(1,len(array)):
        j = i - 1
        aux = array[i]
        while j >= 0 and aux < array[j]:
            array[j+1],array[j] = array[j],array[j+1]
            j -= 1
    return array

while quantidade > 0:
    numero = int(input())
    if numero in ocorrencias:
        ocorrencias[numero] += 1
    else:
        ocorrencias[numero] = 1
        array.append(numero)
    quantidade -= 1
array = insertionSort(array)

for i in range(len(array)):
    print(f'{array[i]} aparece {ocorrencias[array[i]]} vez(es)')