# Receber os dados em uma lista
array = input().split()
array2 = array[:]
for count, element in enumerate(array):
    array[count] = int(array[count])
    array2[count] = int(array2[count])
array.sort()
for count, element in enumerate(array):
    print(array[count])
array.reverse()
print()
for count, element in enumerate(array2):
    print(array2[count])