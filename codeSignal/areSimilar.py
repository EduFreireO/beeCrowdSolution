# Para caracterizar troca --> As posições precisam ser diferentes ou nao existir aquele elemento
def solution(a,b):
    diferrences = 0
    index = 0
    while index < len(a):
        if a[index] != b[index]:
            diferrences += 1
            if diferrences > 2 or a[index] not in b or b[index] not in a: return False
            index += 1
        else:
            a.pop(index), b.pop(index)
    return True

