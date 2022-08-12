def solution(a):
    comprimento = len(a)
    for index in range(comprimento):
        if a[index] == -1:
            continue
        for j in range(index + 1, comprimento):
            if a[index] > a[j] and a[j] != - 1 :
                a[index], a[j] = a[j], a[index]  
    return a     