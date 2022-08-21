function solution(inputArray, k) {
    let maiorSoma = 0
    let soma;
    let i;    
    for(i = 0; i < (inputArray.length - (k + 1)); i ++){
        soma = inputArray[i]
        for(let b = 1; b <= k; b++){
            soma += inputArray[i + b]  
        }
        if(soma > maiorSoma)
            maiorSoma = soma
    }
    return maiorSoma        
}   
