#Ord / count na ord - 1
def solution(inputString):
    inputString = list(inputString)
    for letra in inputString:
       if ord(letra) > 97 and inputString.count(letra) > inputString.count(chr(ord(letra)- 1)):
        return False 
    return True        
