function solution(inputArray, k) {
    let contador = 0
    return inputArray.filter((item, contador) =>{ 
        (++contador)% k != 0?inputArray[contador]:contador)

    }
}