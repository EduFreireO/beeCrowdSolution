def solution(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    comum = 0
    for letra in s1:
        if letra in s2:
            comum += 1
            s2.remove(letra)
    return comum 
         