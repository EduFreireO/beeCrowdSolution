function solution(inputString){
    inputString = (inputString.split(''))
    inputString = inputString.map((letra) => {
        let auxiliar = (letra.charCodeAt() - 96) % 26 + 97
        return letra = String.fromCharCode(auxiliar)
    })
    
    return inputString.join('')
}
// better way
function solution2(inputString){
    const alphabet =  "abcdefghijklmnopqrstuvwxyz"
return inputString.split('').map(elem => 
    alphabet[alphabet.indexOf(elem) < 25?( alphabet.indexOf(elem) + 1):0]).join('')
}