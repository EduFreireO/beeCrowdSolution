function solution(inputString) {
    const number =  inputString.match(/[0-9][0-9]*/g)
    if(!number)
        return false
    return number.reduce((acc, value) => {
        return acc + Number(value) },0)
}
