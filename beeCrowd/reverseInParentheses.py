def solution(inputString):
    inputString = list(inputString)
    for letra in (inputString):
        if not letra.isalpha():
            inputString.remove(letra)
    return ''.join(inputString[::-1])
print(solution())          
