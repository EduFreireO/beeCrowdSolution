function solution(inputArray, elemToReplace, substitutionElem) {
   return inputArray.map(elemt => elemt == elemToReplace? substitutionElem: elemt) 
}

