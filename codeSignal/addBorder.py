def solution(a):
    line = '*' * (len(a[0]) + 2)
    for elemento in range(len(a)):
        a[elemento] = '*' + a[elemento] + '*'
    return [line] + a + [line]


