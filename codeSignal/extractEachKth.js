function solution(inputArray, k) {
    newArray = []
    for(let i = 0; i < inputArray.length; i++){
        if((i + 1) % k != 0)
            newArray.push(inputArray[i])
    }
    return newArray
}
function solution2(inputArray, k){
    return inputArray.filter((current, index) => index % k) // works like a bool value
}