function solution(inputString) {
    let digit = /[0-9]/
    for(let i of inputString.split('')){
        if(digit.test(i))
            return i
    }
}
