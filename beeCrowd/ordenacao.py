import  time
# Bubble sort.
# Sempre coloca os maiores elementos para o final.
incio = time.time()
def bubbleSort(array):
    comprimento = len(array)
    for i in range(comprimento - 1, 0,-1):
        for j in range(i):
            if array[j] > array[j + 1]:
                (array[j], array[j+1]) = (array[j+1], array[j])
    return  array
fim = time.time()
print(f'Bubble sort {fim - incio }')
#variavel = bubbleSort([3,2,9,1,7])
#print(variavel)

# Selection Sort --> busca ordenar os pelos menores
incio = time.time()
def selectionSort(array):
    comprimento = len(array)
    for i in range(comprimento - 1):
        for j in range(i + 1 , comprimento):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return  array
fim = time.time()
print(f'selection sort {fim - incio }')

incio = time.time()
def insertionSort(array):
   n = len(array)
   for i in range(1,n):
       aux = array[i]
       j = i - 1
       while j >= 0 and array[j] > aux:
           array[j + 1], array[j] = array[j], array[j+1]
           j -= 1
   return array
fim = time.time()

print(f'insection sort {fim - incio }')
print(insertionSort([4,7,2,5,4,0]))